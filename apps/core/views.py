from django.shortcuts import render
from apps.dashboard.models import Photos, Our, Events
from apps.dashboard.forms import PhotoForm

def index(request):
  data = {}
  data['photos'] = Photos.objects.all()
  data['our'] = Our.objects.get(pk=1)
  data['events'] = Events.objects.all()
  return render(request, 'core/index.html', data)