from django.shortcuts import render
from eventosv.apps.evento.models import *
from eventosv.apps.evento.forms import *
from django.views.generic import *
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
# Create your views here.
#CREAR un nuevo evento----------------------
class EventoCreate(CreateView):
    template_name = "evento/crear.html"
    model = Evento
    form_class = EventoForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.creador = self.request.user
        f.save()
        invitados = form.cleaned_data['invitados']
        if invitados.count() > 0:
            for i in invitados:
                I = Invitacion()
                I.evento = f
                I.invitado = i
                I.save()
        return super(CreateView, self).form_valid(form)

#ACTUALIZAR el evento----------------------
class EventoUpdate(UpdateView):
    template_name = "evento/actualizar.html"
    model = Evento
    form_class = EventoForm

#ELIMINAR el evento----------------------
class EventoDelete(DeleteView):
    template_name = "evento/eliminar.html"
    model = Evento
    success_url = reverse_lazy('evento_list')

#LISTA de eventos----------------------
class EventoListView(ListView):
    template_name = "evento/lista.html"
    #queryset = Evento.objects.filter(privado = False)
    model = Evento

    def get_context_data(self, **kwargs):
        context = super(EventoListView, self).get_context_data(**kwargs)
        eventos = Evento.objects.all()
        comentarios = []
        #Por cada juego, obtener sus ultimas 4 opiniones
        for e in eventos:
            l = Comentario.objects.filter(evento = e).reverse().order_by('id')[:4]
            #Una vez obtenidas las opiniones, cada una de ellas se agrega a la lista
            for i in l:
                comentarios.append(i)
        #finalmente el contexto tendra el valor de la lista
        context['el_comentario'] = comentarios
        return context



#DETALLE de un evento----------------------
class EventoDetailView(DetailView):
    template_name = "evento/detalle.html"
    model = Evento


    def get_context_data(self, **kwargs):
        context = super(EventoDetailView, self).get_context_data(**kwargs)

        context['la_invi'] = Invitacion.objects.filter(estado="")
        return context


#CREAR una opinion
class ComentarioCreate(CreateView):
    template_name = 'comentario/crear.html'
    model = Comentario
    form_class = ComentarioForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ComentarioCreate, self).get_context_data(**kwargs)
        context['titulo'] = Evento.objects.get(id=self.kwargs['pk'])
        context['id'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usuario = self.request.user
        e = Evento.objects.get(id=self.kwargs['pk'])
        obj.evento = e
        obj.save()
        return super(ComentarioCreate, self).form_valid(form)




#ACEPTAR O NO LA  invitacion---------------------
class InvitacionUpdate(UpdateView):
    template_name = "mensajes/invitacion.html"
    model = Invitacion
    form_class = InvitacionForm
    success_url = "/"



def EventoJoin(request, pk):
    if request.user.is_authenticated():
        evento = Evento.objects.get(id = pk)
        if evento.confirmados.count() == evento.espacios:
            return HttpResponseRedirect('/')
        else:
            if evento.permiso_para_entrar == True:
                solicitud = Solicitud.objects.filter(evento = evento, solicitante = request.user, estado = '')
                if solicitud.count() == 0:
                    S = Solicitud()
                    S.evento = evento
                    S.solicitante = request.user
                    S.save()
                    return HttpResponseRedirect('/evento/list/')
                else:
                    return HttpResponseRedirect('/')
            else:
                evento.confirmados.add(request.user)
                return HttpResponseRedirect('/evento/list/')
    else:
        return HttpResponseRedirect('/accounts/login/')
