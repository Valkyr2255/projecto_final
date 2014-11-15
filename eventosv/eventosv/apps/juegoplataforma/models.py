from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.
class Plataforma(models.Model):
	nombre = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('plataforma_detail', kwargs={'pk': self.pk})


def path(self, filename):
	path_ = "juego/%s/%s"%(self.nombre, filename)
	return path_

class Juego(models.Model):
	nombre = models.CharField(max_length = 40)
	descripcion = models.CharField(max_length = 1500)
	fecha_lanzamiento = models.DateField(null = True)
	url = models.URLField()
	tipos = (
		('C','Juego Completo'),
		('M','Mod'),
		)
	tipo = models.CharField(max_length=1, choices = tipos, default = 'C')
	portada = models.ImageField(upload_to = path)
	plataformas = models.ManyToManyField(Plataforma)

	def __unicode__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('juego_detail', kwargs={'pk': self.pk})

class Opinion(models.Model):
	juego = models.ForeignKey(Juego)
	usuario = models.ForeignKey(User)
	opinion = models.CharField(max_length=250)
	tipos = (
		('Positiva', 'Positiva'),
		('Negativa', 'Negativa')
		)
	tipo = models.CharField(max_length=8, choices = tipos, default='Positiva')

	class Meta:
		unique_together = (('juego','usuario'),)

	def __unicode__(self):
		return "Opinion, %s - %s"%(self.juego,self.usuario.username)