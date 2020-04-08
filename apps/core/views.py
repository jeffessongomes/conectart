from django.shortcuts import render
from apps.dashboard.models import Photos
from apps.dashboard.forms import PhotoForm

def index(request):
  data = {}
  data['photos'] = Photos.objects.all()
  return render(request, 'core/index.html', data)