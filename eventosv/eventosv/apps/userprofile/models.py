from django.db import models
from django.db.models import signals
from eventosv.apps.juegoplataforma.models import Plataforma
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

def path(self, filename):
	path_ = "user/%s/%s"%(self.usuario.username, filename)
	return path_

class UserProfile(models.Model):
	usuario = models.OneToOneField(User)
	imagen = models.ImageField(upload_to = path, null = True, blank = True)
	plataformas = models.ManyToManyField(Plataforma, null = True)

	def __unicode__(self):
		return self.usuario.username



def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(usuario=instance)

signals.post_save.connect(create_user_profile, sender=User)


