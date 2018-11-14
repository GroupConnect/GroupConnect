from django.shortcuts import render
from django.views import generic
from GroupConnect.models import Account
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'GroupConnect/index.html'

class SettingView(generic.TemplateView):
    template_name = 'GroupConnect/mysetting.html'

    def get_context_data(self, **kwags):
        context = super().get_context_data(**kwags)
        context ['acc'] = Account.objects.get(id=1)
        return context