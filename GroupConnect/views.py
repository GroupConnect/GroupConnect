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

def signboard_page_view(request, pk, selected_id=None):
    signboard = get_object_or_404(Signboard, pk=pk)

    # form = forms.PostCreateForm(request.POST or None)
    if request.method == 'POST':
        # form.save()
            
        new_post = Post(
            signboard_id=signboard,
            contributer=get_object_or_404(Member, pk=1)
        )
        if 'post_text' in request.POST:
            new_post.text = request.POST['post_text']
        elif 'reply_text' in request.POST:
            reply_source_id = int(request.POST['reply_source'])
            new_post.reply = get_object_or_404(Post, pk=reply_source_id)
            new_post.text = request.POST['reply_text']

        if 'attached_file' in request.POST:
            new_post.attached_file = request.POST['attached_file']

        new_post.save()

        if selected_id:
            for query in Signboard.objects.filter(pk=pk).prefetch_related('post_set'):
                post = query.post_set.get(pk=int(selected_id))
                post_list = collect_reply(post)
        else:
            for query in Signboard.objects.filter(pk=pk).prefetch_related('post_set'):
                post_list = query.post_set.all().order_by('-created_at')

        situation_list = {}
        situation_list['read_counter'] = 0
        situation_list['read_members'] = []
        for post in post_list:
            read_list = situation_counter(post)
            situation_list['read_counter'] = read_list[0]
            situation_list['read_members'] = read_list[1]

        return render(request, 'GroupConnect/bord.html', context= {
            'signboard': signboard,
            'post_list': post_list,
            'situation_list': situation_list
        })
    
    else:

        if selected_id:
            for query in Signboard.objects.filter(pk=pk).prefetch_related('post_set'):
                post = query.post_set.get(pk=int(selected_id))
                post_list = collect_reply(post)
        else:
            for query in Signboard.objects.filter(pk=pk).prefetch_related('post_set'):
                post_list = query.post_set.all().order_by('-created_at')

        situation_list = {'read_counter': 0, 'read_members': []}
        for post in post_list:
            read_list = situation_counter(post)
            situation_list['read_counter'] = read_list[0]
            situation_list['read_members'] = read_list[1]

        return render(request, 'GroupConnect/bord.html', context= {
            'signboard': signboard,
            'post_list': post_list,
            'situation_list': situation_list
        })
    
def situation_counter(post):
    read_counter = 0
    read_members = []

    for post in Post.objects.filter(pk=post.id).prefetch_related('situation_set'):
        for situation in post.situation_set.all():
            if situation.read_situation:
                read_counter += 1
                read_members.append(situation.user_id)
        else:
            if post.read_number != read_counter:
                post.read_number = read_counter
                post.save()

    return read_counter, read_members

def collect_reply(post):
    post_list = []
    reply_from = []
    reply = []

    post_list.append(post)
    
    for post_related in Post.objects.filter(pk=post.id).prefetch_related('post_set'):
        reply = post_related.post_set.all().order_by('-created_at')

    post_list.extend(reply)

    while True:
        if post.reply:
            reply_from.append(post.reply)
            post = post.reply
        else:
            break
    
    reply_from.extend(post_list)

    post_list = reply_from

    return post_list

class MypageView(generic.TemplateView):
    template_name = 'GroupConnect/mypage.html'

class GrouptopView(generic.TemplateView):
    template_name = 'GroupConnect/grouptop.html'

class BordView(generic.TemplateView):
    template_name = 'GroupConnect/bord.html'
