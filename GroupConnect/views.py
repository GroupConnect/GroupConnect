from django.shortcuts import render
from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'GroupConnect/index.html'

from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template.loader import get_template
from django.views import generic
from .forms import (
    LoginForm, UserCreateForm, GroupCreateForm , CreateSignboardForm
)
from .models import (
    Notice, Group, Member, GroupIcon,Signboard,Post,Situation
)

from django.views.generic.edit import ModelFormMixin


User = get_user_model()

class bordlist(generic.CreateView) :
    template_name = 'GroupConnect/bordlist.html'
    form_class = CreateSignboardForm
    context_object_name='group_list'


    def form_valid(self,form):
        """ 掲示板作成 """
        signboard = form.save(commit = False)
        signboard.group_id= 1
        signboard.save()


        return redirect('GroupConnect:bordlist')


    
    def get_context_data(self, **kwargs):

        

        context = super().get_context_data(**kwargs)
        context.update({
            'messages' : Signboard.objects.all()
        })
        return context

    def get_queryset(self):
        ID = self.request.user.id

        

        members = Member.objects.filter(user_id=ID)
        
        g = []

        for i in members:
            groups = Group.objects.all().filter(id=i.group_id)
            g += groups


        return g





        
