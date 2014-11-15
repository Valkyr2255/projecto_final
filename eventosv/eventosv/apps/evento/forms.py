from django import forms 
from eventosv.apps.evento.models import *

class EventoForm(forms.ModelForm):
	class Meta:
		model = Evento
		exclude = ('creador','confirmados')	

	def __init__(self, *args, **kwargs):
		super(EventoForm, self).__init__(*args, **kwargs)
		self.fields['permiso_para_entrar'].help_text = 'Determina si cualquier usuario puede entrar al evento o necesita confirmacion por parte del creador'
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			if field == 'fecha':
				self.fields[field].widget.attrs['readonly'] = ''


	def clean(self):
		cleaned_data = super(EventoForm, self).clean()
		e = cleaned_data['espacios']
		i = cleaned_data['invitados']
		j = cleaned_data['juego']
		p = cleaned_data['plataforma']
		c = i.count()
		if c>e:
			raise forms.ValidationError(
				('El evento solo tiene %(espacios)s y se han invitado a %(invitados)s usuarios'),
				code = 'invalido',
				params = {'espacios':e,'invitados':c},
				)
		if p not in j.plataformas.all():
			raise forms.ValidationError(
				('El juego seleccionado no esta disponible para la plataforma seleccionada'),
				code = 'invalido',
				)


class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = ['comentario']
		widgets = {
			'comentario': forms.Textarea()
		}

	def __init__(self, *args, **kwargs):
		super(ComentarioForm, self).__init__(*args, **kwargs)
		self.fields['comentario'].help_text = '* Maximo 250 caracteres por opinion'
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'




class InvitacionForm(forms.ModelForm):
	class Meta:
		model = Invitacion
		exclude = ('invitado','evento')	

	def __init__(self, *args, **kwargs):
		super(InvitacionForm, self).__init__(*args, **kwargs)
		self.fields['estado'].help_text = 'Eres libre de aceptar o rechazar esta invitacion'
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'