from django.shortcuts import render, redirect
from django.views import generic
from GroupConnect.models import Account
from GroupConnect.forms import MyForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.views import(
    PasswordChangeView, PasswordChangeDoneView
)
from django.urls import reverse_lazy
from GroupConnect.forms import(
    MyPasswordChangeForm
)
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'GroupConnect/index.html'

class SettingView(generic.TemplateView):
    template_name = 'GroupConnect/mysetting.html'

class PasswordChange(PasswordChangeView):
    """パスワード変更ビュー"""
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('GroupConnect:password_change_done')
    template_name = 'GroupConnect/password_change.html'

class PasswordChangeDone(PasswordChangeDoneView):
    """パスワード変更しました"""
    template_name = 'GroupConnect/password_change_done.html'

    def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('change_password')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'GroupConnect/change_password.html', {
            'form': form
        })
    
    
    
    '''def form_test(request):
        form  = MyForm(request.POST or None)
        if form.is_valid():
            models.Account.objects.create(**form.cleaned_data)
            return redirect('GroupConnect:mysetting')
        d = {
            'form' : form,
            'account': Account.objects.all().order_by('-id'),
        }
        return render(request, template_name, d)'''

    
    
    '''def form_test(request):
        form = MyForm()
        return render(request, template_name, {
            'form': form,
        })'''

    '''def get_context_data(self, **kwags):
        context = super().get_context_data(**kwags)
        context ['acc'] = Account.objects.get(id=1)
        return context'''
