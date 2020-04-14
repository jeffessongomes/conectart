from django.shortcuts import render, redirect
from apps.dashboard.models import Photos, Our, Events, Client, Comments
from apps.dashboard.forms import PhotoForm, ClientForm, CommentForm

from django.http import HttpResponse
import json


def index(request):
  data = {}
  data['photos'] = Photos.objects.all()
  data['our'] = Our.objects.get(pk=1)
  data['events'] = Events.objects.all()
  return render(request, 'core/index.html', data)


def event(request, pk):
  data = {}
  data['event'] = Events.objects.get(pk=pk)
  return render(request, 'core/event.html', data)



def add_client(request, pk):
  data = {}
  event = Events.objects.get(pk=pk)

  if request.method == 'POST':
    form = ClientForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      form.save()

      return redirect('index')
    else:
      HttpResponse(json.dumps(form.errors))
  else:
    form = ClientForm(initial={'events':event.pk})
  data['form'] = form; data['event'] = event

  return render(request, 'core/client.html', data)



def comments(request):
  data = {}
  if request.method == 'POST':
    form = CommentForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      form.save()
      #send_email(request)

      return redirect('index')
    else:
      return HttpResponse(json.dumps(form.errors))
  else:
      return HttpResponse("<h1>Mensagem não enviada</h1>")