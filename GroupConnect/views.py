from django.shortcuts import render
from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'GroupConnect/index.html'

class MypageView(generic.TemplateView):
    template_name = 'GroupConnect/mypage.html'

class LogoutView(generic.TemplateView):
    template_name = 'GroupConnect/logout.html'

class GrouptopView(generic.TemplateView):
    template_name = 'GroupConnect/grouptop.html'

class BordView(generic.TemplateView):
    template_name = 'GroupConnect/bord.html'