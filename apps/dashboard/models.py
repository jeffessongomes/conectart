from django.db import models
from django.contrib.auth.models import User



class Admin(models.Model):
	name = models.CharField(max_length=500)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=30)



class Events(models.Model):
	name = models.CharField('nome', max_length=500)
	details = models.TextField('detalhes')
	city = models.CharField('cidade', max_length=500)
	district = models.CharField('bairro', max_length=500)
	street = models.CharField('rua', max_length=500, help_text=('Nome da rua e o número da habitação'))
	day = models.CharField('dia', max_length=500)
	hour = models.CharField('hora', max_length=500)
	main_image = models.ImageField('imagem principal', upload_to='image_event')
	image_2 = models.ImageField('imagem 2', upload_to='image_event', null=True, blank=True, help_text=('Imagem não obrigatória. '))
	image_3 = models.ImageField('imagem 3', upload_to='image_event', null=True, blank=True, help_text=('Imagem não obrigatória. '))
	
	def __str__(self):
		return self.name

class Client(models.Model):
	name = models.CharField(max_length=500)
	email = models.EmailField()
	events = models.ForeignKey(Events, on_delete=models.CASCADE, null=True, blank=True)

class Comments(models.Model):
	email = models.EmailField()
	title = models.CharField(max_length=500)
	whatsapp = models.CharField(max_length=100, null=True)
	details = models.TextField()

	def __str__(self):
		return self.title

class Subscribe_User(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	events = models.ForeignKey(Events, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user)+" / "+str(self.events)

class Photos(models.Model):
	image = models.ImageField('Imagem', upload_to='image')
	
class TecDashImages(models.Model):
	title = models.CharField(max_length=500, null=True)
	slug = models.CharField(max_length=100, null=True)
	details = models.TextField()
	image = models.ImageField(upload_to='image/dash')

	def __str__(self):
		return self.title

class Our(models.Model):
	details = models.TextField('detalhes')