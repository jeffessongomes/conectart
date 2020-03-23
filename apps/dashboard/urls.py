from django.urls import path

from . import views

urlpatterns = [
  
	path('login', views.do_login, name="login"),
	path('logout', views.do_logout, name="logout"),

	path('forget_password', views.forget_password, name='forget_password'),
	path('confirme_password/<int:pk>/<str:token>', views.confirme_password, name='confirme_password'),
	path('change_password', views.change_password, name='change_password'),

  	# crud event
	path('add_event', views.add_event, name="add_event"),
	path('edit_event/<int:pk>', views.edit_event, name="edit_event"),
	path('list_event', views.list_event, name="list_event"),
	path('delete_event/<int:pk>', views.delete_event, name="delete_event"),

]










