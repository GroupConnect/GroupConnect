from django.shortcuts import render
from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'GroupConnect/index.html'

class Temp_entryView(generic.TemplateView):
    template_name = 'GroupConnect/temp_entry.html'

class Temp_entry_resultView(generic.TemplateView):
    template_name = 'GroupConnect/temp_entry_result.html'

class MypageView(generic.TemplateView):
    template_name = 'GroupConnect/mypage.html'

class GrouptopView(generic.TemplateView):
    template_name = 'GroupConnect/grouptop.html'

class BordlistView(generic.TemplateView):
    template_name = 'GroupConnect/bordlist.html'

class BordView(generic.TemplateView):
    template_name = 'GroupConnect/bord.html'

class NotFoundView(generic.TemplateView):
    template_name = 'GroupConnect/notfound.html'