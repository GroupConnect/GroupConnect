from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from .forms import LoginForm
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'GroupConnect/index.html'

class Top(generic.TemplateView, LoginView):
    form_class = LoginForm
    template_name = 'GroupConnect/top.html'
 
 
class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'GroupConnect/top.html'
 