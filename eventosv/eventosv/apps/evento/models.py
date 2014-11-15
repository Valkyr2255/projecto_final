from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import datetime 
from eventosv.apps.juegoplataforma.models import *

# Create your models here.
class Evento(models.Model):
	titulo = models.CharField(max_length = 30)
	descripcion = models.CharField(max_length = 300)
	mensaje_secreto = models.CharField(max_length = 200, null = True)
	creador = models.ForeignKey(User,related_name="creador")
	juego = models.ForeignKey(Juego)
	plataforma = models.ForeignKey(Plataforma)
	espacios = models.IntegerField()
	privado = models.BooleanField(default = False)
	invitados = models.ManyToManyField(User,related_name="invitados", null = True, blank = True)
	fecha = models.DateTimeField()
	confirmados = models.ManyToManyField(User, related_name = 'confirmados', null = True, blank = True)
	permiso_para_entrar = models.BooleanField(default = False)

	def __unicode__(self):
		return "%s, %s, %s, %s"%(self.titulo, self.creador, self.juego, self.plataforma)

	def get_absolute_url(self):
		return reverse('evento_detail', kwargs={'pk': self.pk})

class Comentario(models.Model):
	evento = models.ForeignKey(Evento)
	usuario = models.ForeignKey(User)
	comentario = models.CharField(max_length = 100)


class Invitacion(models.Model):
	evento = models.ForeignKey(Evento)
	invitado = models.ForeignKey(User, related_name = 'invitado')
	#fecha = models.DateTimeField(default=datetime.now(),blank=True)
	estados = (
		('',''),
		('Aceptada','Aceptada'),
		('Rechazada','Rechazada')
		)
	estado = models.CharField(max_length = 9, choices = estados, default ='')

	def __unicode__(self):
		return "%s - %s"%(self.evento, self.invitado)

class Solicitud(models.Model):
	evento = models.ForeignKey(Evento)
	solicitante = models.ForeignKey(User)
	estados = (
		('',''),
		('Aceptada','Aceptada'),
		('Rechazada','Rechazada')
		)
	estado = models.CharField(max_length = 9, choices = estados, default ='')

	def __unicode__(self):
		return "%s - %s"%(self.evento, self.solicitante)