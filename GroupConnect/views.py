from django.shortcuts import render, redirect
from django.views import generic
from GroupConnect.models import Account
from GroupConnect.forms import MyForm
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'GroupConnect/index.html'

class SettingView(generic.TemplateView):
    template_name = 'GroupConnect/mysetting.html'

    def form_test(request):
        form  = MyForm(request.POST or None)
        '''if form.is_valid():
            models.Account.objects.create(**form.cleaned_data)
            return redirect('GroupConnect:mysetting')'''
        d = {
            'form' : form,
            'account': Account.objects.all().order_by('-id'),
        }
        return render(request, template_name, d)
    
    '''def form_test(request):
        form = MyForm()
        return render(request, template_name, {
            'form': form,
        })'''

    '''def get_context_data(self, **kwags):
        context = super().get_context_data(**kwags)
        context ['acc'] = Account.objects.get(id=1)
        return context'''
