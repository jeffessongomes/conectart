from django.db import models
from django.contrib.auth.models import User



class Admin(models.Model):
	name = models.CharField(max_length=500)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=30)

class Events(models.Model):
	name = models.CharField(max_length=500)
	details = models.TextField()
	city = models.CharField(max_length=500)
	district = models.CharField(max_length=500)
	street = models.CharField(max_length=500)
	day = models.CharField(max_length=500)
	hour = models.CharField(max_length=500)
	main_image = models.ImageField(upload_to='image_product')
	image_2 = models.ImageField(upload_to='image_product', null=True, blank=True)
	image_3 = models.ImageField(upload_to='image_product', null=True, blank=True)
	
	def __str__(self):
		return self.name

class Subscribe_User(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	events = models.ForeignKey(Events, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user)+" / "+str(self.events)

class Photos(models.Model):
	image = models.ImageField(upload_to='image')
	