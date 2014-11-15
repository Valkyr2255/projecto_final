from django.shortcuts import render
from django.http import HttpResponse
from eventosv.apps.evento.models import *
import json

from django.forms.models import model_to_dict
from django.core import serializers
# Create your views here.

def wsInvitaciones_view(request):
	i_query = Invitacion.objects.select_related('invitado').filter(invitado=request.user,estado="")
	e_query = Evento.objects.all()
	u_query = User.objects.all()
	e1 = serializers.serialize('json', e_query )
	e_list = json.loads( e1 )
 
	i1 = serializers.serialize("json",[x for x in i_query])
	i_list = json.loads( i1 )

	u1 = serializers.serialize('json', u_query )
	u_list = json.loads( u1 )
    
	data = json.dumps( {'i':i_list,'e':e_list,'u':u_list} )
	return HttpResponse (data,content_type="application/json")


def wsEventos_view(request):
	i_query = Invitacion.objects.select_related('invitado').filter(invitado=request.user,estado="Aceptada")
	e_query = Evento.objects.all()
	u_query = User.objects.all()
	e1 = serializers.serialize('json', e_query )
	e_list = json.loads( e1 )
 
	i1 = serializers.serialize("json",[x for x in i_query])
	i_list = json.loads( i1 )

	u1 = serializers.serialize('json', u_query )
	u_list = json.loads( u1 )
    
	data = json.dumps( {'i':i_list,'e':e_list,'u':u_list} )
	return HttpResponse (data,content_type="application/json")
























# 	from django.shortcuts import render
# from django.http import HttpResponse
# from eventosv.apps.evento.models import *

# from django.core import serializers
# # Create your views here.

# def wsInvitaciones_view(request):
# 	#all_objects = list(Invitacion.objects.filter(invitado=request.user,estado="")

# 	#A = list(Invitacion.objects.filter(invitado=request.user,estado=""))

# 	#B = list(Evento.objects.all())
# 	#all_objects = A + B



# 	e = Invitacion.objects.select_related('invitado').filter(invitado=request.user,estado="")




# 	data = serializers.serialize("json",[x for x in e])
# 	return HttpResponse (data,content_type="application/json")