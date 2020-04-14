from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('event/<int:pk>', views.event, name="event"),
  path('add_client/<int:pk>', views.add_client, name="add_client"),
  path('comments', views.comments, name="comments"),
]