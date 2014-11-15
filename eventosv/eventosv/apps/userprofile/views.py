from django.shortcuts import render
from eventosv.apps.userprofile.forms import *
from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from eventosv.apps.userprofile.models import *
from eventosv.apps.userprofile.forms import *
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy


from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views import *

from django.views.generic.edit import ProcessFormView

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
# Create your views here.

#CREAR un nuevo usuario----------------------
class SignUpView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = "/accounts/login/"


class LoginView(FormView):
    form_class = LoginForm
    template_name="accounts/login.html"
    success_url = "/"
    def form_valid(self, form):
    	login(self.request, form.get_user())
    	return super(LoginView, self).form_valid(form)

class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


#EDITAR TU PERFIL
class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    template_name = "accounts/profile.html"
    success_url = "/"
