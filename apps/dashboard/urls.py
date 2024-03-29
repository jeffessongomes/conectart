from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name="home"),	

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

	# crud 
	path('add_photo', views.add_photo, name="add_photo"),
	path('edit_photo/<int:pk>', views.edit_photo, name="edit_photo"),
	path('list_photo', views.list_photo, name="list_photo"),
	path('delete_photo/<int:pk>', views.delete_photo, name="delete_photo"),

	path('edit_our', views.edit_our, name="edit_our"),

	path('list_subscribe/<int:pk>', views.list_client, name="list_subscribe"),
	path('choose_event', views.choose_event, name="choose_event"),


	path('list_comment', views.list_comment, name="list_comment"),
	
]










