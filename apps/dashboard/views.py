from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from .tokens import account_activation_token



def verifify_user(email, password):
  try:
    user = User.objects.get(email=email)
  except User.DoesNotExist:
    user = None
    
  if user is not None:
    user = authenticate(username=user.username, password=password)
    return user
  else:
    return user

def do_login(request):
  
  if request.method == 'POST':
    email = request.POST['email']; 
    password = request.POST['password'];
    user = verifify_user(email, password) 
        
    if user is not None:
      login(request, user)
      return redirect('index')
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
          'entrego.oficialdelivery@gmail.com', # 'from'
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
