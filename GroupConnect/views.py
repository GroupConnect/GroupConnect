from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import redirect, resolve_url
from django.template.loader import get_template
from django.views import generic
from .forms import (
    LoginForm, UserCreateForm, UserUpdateForm, UserMailaddressUpdateForm
)
from .models import (
    Notice, Group, Member
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

class NoticeDetail(generic.DetailView):
    model = Notice
    template_name = 'GroupConnect/notice_detail.html'

    def index(self, request):
        return Notice.objects.filter(id = request.notice.id)

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


class UserDetail(OnlyYouMixin, generic.DetailView):
    model = User
    template_name = 'GroupConnect/user_detail.html'


class UserUpdate(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'GroupConnect/user_form.html'

    def get_success_url(self):
        return resolve_url('GroupConnect:user_update', pk=self.kwargs['pk'])

    context_object_name = 'rogin_user'

    def get_queryset(self):
        ID = self.request.user.id
        user = User.objects.filter(id = ID)

        return user

class UserMailaddressUpdate(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserMailaddressUpdateForm
    template_name = 'GroupConnect/user_mailaddress_update.html'

    def get_success_url(self):
        return resolve_url('GroupConnect:user_mailaddress_update', pk=self.kwargs['pk'])

    context_object_name = 'rogin_user'

    def get_queryset(self):
        ID = self.request.user.id
        user = User.objects.filter(id = ID)

        return user