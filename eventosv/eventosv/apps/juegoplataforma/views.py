from django.shortcuts import render
from django import forms 
from eventosv.apps.juegoplataforma.models import *
from eventosv.apps.juegoplataforma.forms import *
from django.views.generic import *
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

#CREAR un nuevo Juego----------------------
class JuegoCreate(CreateView):
    template_name = "juego/crear.html"
    model = Juego
    form_class = JuegoForm



#ACTUALIZAR el Juego----------------------
class JuegoUpdate(UpdateView):
    template_name = "juego/actualizar.html"
    model = Juego
    form_class = JuegoForm

#ELIMINAR el Juego----------------------
class JuegoDelete(DeleteView):
    template_name = "juego/eliminar.html"
    model = Juego
    success_url = reverse_lazy('juego_list')

#LISTA de Juegos----------------------
class JuegoListView(ListView):
    template_name = "juego/lista.html"
    model = Juego

    def get_context_data(self, **kwargs):
        context = super(JuegoListView, self).get_context_data(**kwargs)
        juegos = Juego.objects.all()
        opiniones = []
        #Por cada juego, obtener sus ultimas 4 opiniones
        for j in juegos:
            l = Opinion.objects.filter(juego = j).reverse().order_by('id')[:4]
            #Una vez obtenidas las opiniones, cada una de ellas se agrega a la lista
            for i in l:
                opiniones.append(i)
        #finalmente el contexto tendra el valor de la lista
        context['la_opinion'] = opiniones
        return context


#DETALLE de un Juego----------------------
class JuegoDetailView(DetailView):
    template_name = "juego/detalle.html"
    model = Juego













#CREAR un nuevo Juego----------------------
class PlataformaCreate(CreateView):
    template_name = "plataforma/crear.html"
    model = Plataforma
    form_class = PlataformaForm



#ACTUALIZAR el plataforma----------------------
class PlataformaUpdate(UpdateView):
    template_name = "plataforma/actualizar.html"
    model = Plataforma
    form_class = PlataformaForm

#ELIMINAR el plataforma----------------------
class PlataformaDelete(DeleteView):
    template_name = "plataforma/eliminar.html"
    model = Plataforma
    success_url = reverse_lazy('plataforma_list')

#LISTA de plataformas----------------------
class PlataformaListView(ListView):
    template_name = "plataforma/lista.html"
    model = Plataforma

#DETALLE de un plataforma----------------------
class PlataformaDetailView(DetailView):
    template_name = "plataforma/detalle.html"
    model = Plataforma







#CREAR una opinion
class OpinionCreate(CreateView):
    template_name = 'opinion/crear.html'
    model = Opinion
    form_class = OpinionForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(OpinionCreate, self).get_context_data(**kwargs)
        context['titulo'] = Juego.objects.get(id=self.kwargs['pk'])
        context['id'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usuario = self.request.user
        j = Juego.objects.get(id=self.kwargs['pk'])
        obj.juego = j
        obj.save()
        return super(OpinionCreate, self).form_valid(form)



class CompletosView(ListView):
    template_name = "juego/completos.html"
    model = Juego

    def get_queryset(self):
        queryset = super(CompletosView, self).get_queryset()
        return queryset.filter(tipo = 'C')

    def get_context_data(self, **kwargs):
        context = super(CompletosView, self).get_context_data(**kwargs)
        juegos = Juego.objects.all()
        opiniones = []
        #Por cada juego, obtener sus ultimas 4 opiniones
        for j in juegos:
            l = Opinion.objects.filter(juego = j).reverse().order_by('id')[:4]
            #Una vez obtenidas las opiniones, cada una de ellas se agrega a la lista
            for i in l:
                opiniones.append(i)
        #finalmente el contexto tendra el valor de la lista
        context['la_opinion'] = opiniones
        return context

class ModsView(ListView):
    template_name = "juego/mods.html"
    model = Juego

    def get_queryset(self):
        queryset = super(ModsView, self).get_queryset()
        return queryset.filter(tipo = 'M')

    def get_context_data(self, **kwargs):
        context = super(ModsView, self).get_context_data(**kwargs)
        juegos = Juego.objects.all()
        opiniones = []
        #Por cada juego, obtener sus ultimas 4 opiniones
        for j in juegos:
            l = Opinion.objects.filter(juego = j).reverse().order_by('id')[:4]
            #Una vez obtenidas las opiniones, cada una de ellas se agrega a la lista
            for i in l:
                opiniones.append(i)
        #finalmente el contexto tendra el valor de la lista
        context['la_opinion'] = opiniones
        return context