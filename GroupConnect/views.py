from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from .forms import (
    LoginForm, UserCreateForm
)
from .models import User

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'GroupConnect/index.html'

class Top(generic.TemplateView, LoginView):
    form_class = LoginForm
    template_name = 'GroupConnect/top.html'
 
 
class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'GroupConnect/top.html'
 
class MailSend(generic.TemplateView):
    template_name = 'GroupConnect/provisional_user_create.html'

class UserCreate(generic.CreateView):
    form_class = UserCreateForm
    template_name = 'GroupConnect/user_create.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()

        return redirect('GroupConnect:top')

class Mypage(generic.TemplateView):
    template_name = 'GroupConnect/mypage.html'