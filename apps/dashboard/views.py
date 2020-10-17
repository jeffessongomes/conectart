from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.http import HttpResponse
import json

from .models import Events, Subscribe_User, Comments, TecDashImages, Our, Photos, Client
from .forms import EventForm, SubscribeForm, OurForm, PhotoForm, ClientForm


# my custom login
def my_login_required(function):
    def wrapper(request, *args, **kw): 
        if not request.session.get('brand_id'):

          return HttpResponseRedirect('/dashboard/login')
        else:
          return function(request, *args, **kw)
    return wrapper




@login_required(login_url='login')
def home(request):
  data = {}

  data['option'] = TecDashImages.objects.all()
  

  return render(request, 'dashboard/dashboard.html', data)  


def verifify_user(email, password):
  try:
    user = User.objects.get(email=email)
  except User.DoesNotExist:
    user = None
    
  if user is not None:
    if user.is_superuser == True:
      user = authenticate(username=user.username, password=password)
      return user
    else:
      user = 0
      return user
  else:
    return user

def do_login(request):
  
  if request.method == 'POST':
    email = request.POST['email']; 
    password = request.POST['password'];
    user = verifify_user(email, password) 
    

    if user is not None:
      if user == 0:
        return HttpResponse("<h1>Você não tem autorização para acessar essa página</h1>")
      else:
        login(request, user)
        return redirect('home')
    else:
      error = True
      return render(request, 'dashboard/telaLogin.html', {'error': error})

  return render(request, 'dashboard/telaLogin.html')

def do_logout(request):
  logout(request)
  return redirect('login')

def forget_password(request):
  if request.method == 'POST':
    try:
      user = User.objects.get(email=request.POST['email'])  
    except User.DoesNotExist:
      user = None
    
    if user != None:
      msg_html = render_to_string('dashboard/email.html', {
        'user': user,
        'token':account_activation_token.make_token(user)
      })
      connection = mail.get_connection()
      connection.open()

      email = mail.EmailMessage(
          'Suporte - Conectart',
          msg_html,   
          'admin@espacoconectar-te.uni5.net', # 'from'
          [user.email,], # 'to'
          connection=connection
      )

      email.send()
      confirmEmail = True
      return render(request, 'dashboard/forget-pass.html', {'confirmEmail': confirmEmail})
    else:
      error = True
      return render(request, 'dashboard/forget-pass.html', {'error': error})
      
  else:
    return render(request, 'dashboard/forget-pass.html')

def confirme_password(request, pk, token):
  try:
    user = User.objects.get(pk=pk)  
  except User.DoesNotExist:
    user = None
  
  if user != None:
    
    if account_activation_token.check_token(user, token):
      return render(request, 'dashboard/change-password.html', {'user_status':user})
    else:
      return HttpResponse("<h1 align='center'>Token does not exist</h1></br></br><a align='center' href='login'>click here</a>")
  else:
    return HttpResponse("<h1 align='center'>User does not exist</h1></br></br><a align='center' href='forget_password'>click here</a>")


def change_password(request):
  if request.method == 'POST':
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 == password2:
      user_status = request.POST['user_status']
      
      try:
        user = User.objects.get(pk=user_status)
      except User.DoesNotExist:
        user = None
      except ValueError:
        user = None

      if user != None:
        user.set_password(password1)
        user.save()

        return redirect('login')
      else:
        return HttpResponse("<h1 align='center'>Please, use the link of your email</h1>")        

    else:
      error = True
      return render(request, 'dashboard/change-password.html', {'error':error})

  error = False
  return render(request, 'dashboard/change-password.html', {'error':error})

def choose_event(request):
  data = {}
  events = Events.objects.all()
  data['events'] = events
  return render(request, 'dashboard/client/choose-event.html', data)


@login_required(login_url='login')
def list_client(request, pk):
  data = {}
  clients = Client.objects.filter(events=pk)
  data['clients'] = clients
  return render(request, 'dashboard/client/list-client.html', data)

@login_required(login_url='login')
def list_comment(request):
  data = {}
  comments = Comments.objects.all()
  data['comments'] = comments
  return render(request, 'dashboard/comments/list-comment.html', data)


# event crud
@login_required(login_url='login')
def add_event(request):
  data = {}
  if request.method == 'POST':
    form = EventForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      form.save()

      return redirect('list_event')
    else:
      HttpResponse(json.dumps(form.errors))
  else:
    form = EventForm()
  data['form'] = form

  return render(request, 'dashboard/event/add-event.html', data)

@login_required(login_url='login')
def list_event(request):
  data = {}
  events = Events.objects.all()
  data['events'] = events
  return render(request, 'dashboard/event/list-event.html', data)

@login_required(login_url='login')
def edit_event(request, pk):
  data = {}
  event = Events.objects.get(pk=pk)
  
  if request.method == 'POST':
    form = EventForm(data=request.POST, files=request.FILES, instance=event)
    if form.is_valid():
      form.save()
      return redirect('home')
    else:
      
      HttpResponse(json.dumps(form.errors))
  else:
    form = EventForm(instance=event)

  data['form'] = form; data['event'] = event;

  return render(request, 'dashboard/event/edit-event.html', data)

@login_required(login_url='login')
def delete_event(request, pk):
  event = Events.objects.get(pk=pk)
  event.delete()
  return redirect('home')


# edit our
@login_required(login_url='login')
def edit_our(request):
  data = {}

  try:
    our = Our.objects.get(pk=1)
  except Our.DoesNotExist:
    our = Our.objects.create(details="escreva aqui o que deverá ficar em 'Sobre o nosso projeto'")
  
  
  if request.method == 'POST':
    form = OurForm(data=request.POST, instance=our)
    if form.is_valid():
      form.save()
      return redirect('home')
    else:
      
     HttpResponse(json.dumps(form.errors))
  else:
    form = OurForm(instance=our)

  data['form'] = form; data['our'] = our;

  return render(request, 'dashboard/our/edit-our.html', data)


# photos crud
@login_required(login_url='login')
def add_photo(request):
  data = {}
  if request.method == 'POST':
    form = PhotoForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      form.save()

      return redirect('list_photo')
    else:
      HttpResponse(json.dumps(form.errors))
  else:
    form = PhotoForm()
  data['form'] = form

  return render(request, 'dashboard/photos/add-photo.html', data)

@login_required(login_url='login')
def list_photo(request):
  data = {}
  photos = Photos.objects.all()
  data['photos'] = photos
  return render(request, 'dashboard/photos/list-photo.html', data)

@login_required(login_url='login')
def edit_photo(request, pk):
  data = {}
  photo = Photos.objects.get(pk=pk)
  
  if request.method == 'POST':
    form = PhotoForm(data=request.POST, files=request.FILES, instance=photo)
    if form.is_valid():
      form.save()
      return redirect('home')
    else:
      
      HttpResponse(json.dumps(form.errors))
  else:
    form = PhotoForm(instance=photo)

  data['form'] = form; data['photo'] = photo;

  return render(request, 'dashboard/photos/edit-photo.html', data)

@login_required(login_url='login')
def delete_photo(request, pk):
  photo = Photos.objects.get(pk=pk)
  photo.delete()
  return redirect('home')