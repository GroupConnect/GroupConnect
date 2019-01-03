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
    LoginForm, UserCreateForm, GroupCreateForm
)
from .models import (
    Notice, Group, Member, GroupIcon
)


User = get_user_model()

class Top(LoginView):
    form_class = LoginForm
    template_name = 'GroupConnect/top.html'





class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'GroupConnect/top.html'

class UserCreate(generic.CreateView):
    template_name = 'GroupConnect/user_create.html'
    form_class = UserCreateForm

    def form_valid(self, form):

        user = form.save(commit=False)
        user.is_active = False
        user.save()

        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': 'https' if self.request.is_secure() else 'http',
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        subject_template = get_template('GroupConnect/mail_template/create/subject.txt')
        subject = subject_template.render(context)

        message_template = get_template('GroupConnect/mail_template/create/message.txt')
        message = message_template.render(context)

        user.email_user(subject, message)
        return redirect('GroupConnect:user_create_done')


class UserCreateDone(generic.TemplateView):
    template_name = 'GroupConnect/user_create_done.html'


class UserCreateComplete(generic.TemplateView):
    template_name = 'GroupConnect/user_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)  # デフォルトでは1日以内

    def get(self, request, **kwargs):
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)

        except SignatureExpired:
            return HttpResponseBadRequest()

        except BadSignature:
            return HttpResponseBadRequest()

        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    user.is_active = True
                    user.save()
                    return super().get(request, **kwargs)

        return HttpResponseBadRequest()



class Mypage(generic.ListView):
    template_name = 'GroupConnect/mypage.html'
    context_object_name = 'group_list'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context.update({
            'notice_list' : Notice.objects.all()
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

def detail(request, notice_id):
    notice = Notice.objects.get(id = notice_id)
    return render(request, 'GroupConnect/notice_detail.html', {'notice':notice})

class GroupCreate(generic.CreateView):
    template_name = 'GroupConnect/group_create.html'
    form_class = GroupCreateForm

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context.update({
            'icon_list' : GroupIcon.objects.all()
        })
        return context

    def form_valid(self, form):
        icon = self.request.POST['icon']
        group = form.save(commit=False)
        group.icon = icon
        group.save()

        groups = Group.objects.all().latest('date_joined')
        group_id = groups.id

        ID = self.request.user.id
        user_name = self.request.user.first_name

        Member(user_id=ID, group_id=group_id, name=user_name, authority=True).save()
        


        return redirect('GroupConnect:mypage')




class GroupTop(generic.DetailView):
    template_name = 'GroupConnect/group_top.html'
    model = Group

    def get_queryset(self):
        ID = self.request.user.id

        members = Member.objects.filter(user_id=ID)
        
        g = []

        for i in members:
            groups = Group.objects.all().filter(id=i.group_id)
            g += groups


        return g

def group(request, group_id):
    group = Group.objects.get(id = group_id)
    return render(request, 'GroupConnect/group_top.html', {'group':group})

def userform(request, user_id):
    user = User.objects.get(id = user_id)
    return render(request, 'GroupConnect/user_form.html', {'user':user})