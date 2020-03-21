from django.urls import path

from . import views

urlpatterns = [
  
  path('login', views.do_login, name="login"),
  path('logout', views.do_logout, name="logout"),

  path('forget_password', views.forget_password, name='forget_password'),
  path('confirme_password/<int:pk>/<str:token>', views.confirme_password, name='confirme_password'),
  path('change_password', views.change_password, name='change_password'),

]










