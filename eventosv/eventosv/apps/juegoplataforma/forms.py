from django import forms 
from eventosv.apps.juegoplataforma.models import *

class JuegoForm(forms.ModelForm):
	class Meta:
		model = Juego
		widgets = {
			'descripcion': forms.Textarea()
		}

	def __init__(self, *args, **kwargs):
		super(JuegoForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			if field != 'portada':
				self.fields[field].widget.attrs['class'] = 'form-control'


class PlataformaForm(forms.ModelForm):
	class Meta:
		model = Plataforma

	def __init__(self, *args, **kwargs):
		super(PlataformaForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'

class OpinionForm(forms.ModelForm):
	class Meta:
		model = Opinion
		fields = ['opinion', 'tipo']
		widgets = {
			'opinion': forms.Textarea()
		}

	def __init__(self, *args, **kwargs):
		super(OpinionForm, self).__init__(*args, **kwargs)
		self.fields['opinion'].help_text = '* Maximo 250 caracteres por opinion'
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'