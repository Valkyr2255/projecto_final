from django.contrib import admin
from eventosv.apps.evento.models import *
# Register your models here.

admin.site.register(Evento)
admin.site.register(Invitacion)
admin.site.register(Comentario)
admin.site.register(Solicitud)
