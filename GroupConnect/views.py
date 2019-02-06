from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Signboard
from . import forms



from django.conf import settings
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
    LoginForm, UserCreateForm, GroupCreateForm
)
from .models import (
    Notice, Group, Member, GroupIcon,Signboard,Post,Situation
)


User = get_user_model()

class bordlist(generic.ListView) :
    template_name = 'GroupConnect/bordlist.html'
    context_object_name='group_list'


    
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





        
class SignboardView(generic.DetailView):
    model = Signboard
    template_name = 'GroupConnect/signboard_detail.html'

def SignboardPage(request, pk):
    signboard = get_object_or_404(Signboard, pk=pk)
    
    for query in Signboard.objects.filter(pk=pk).prefetch_related('post_set'):
        post_list = query.post_set.all()

    form = forms.PostCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return render(request, 'GroupConnect/boad.html', context= {
            'signboard': signboard,
            'post_list' : post_list,
            'form': form
        })
    
    else:
        return render(request, 'GroupConnect/bord.html', context= {
            'signboard': signboard,
            'post_list' : post_list,
            'form': form
        })
class MypageView(generic.TemplateView):
    template_name = 'GroupConnect/mypage.html'

class GrouptopView(generic.TemplateView):
    template_name = 'GroupConnect/grouptop.html'

class BordView(generic.TemplateView):
    template_name = 'GroupConnect/bord.html'
