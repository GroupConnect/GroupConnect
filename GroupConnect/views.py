from django.shortcuts import render
from django.views import generic

from .models import Signboard

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'GroupConnect/index.html'

class SignboardView(generic.DetailView):
    model = Signboard
    template_name = 'GroupConnect/signboard_detail.html'
