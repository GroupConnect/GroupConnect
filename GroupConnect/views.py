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
    LoginForm, UserCreateForm, GroupCreateForm, UserUpdateForm,GroupUpdateForm
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

        """
            お知らせ一覧の取得。
        """
        context = super().get_context_data(**kwargs)
        context.update({
            'notice_list' : Notice.objects.all()
        })
        return context

    def get_queryset(self):
        """
        所属グループ一覧の取得
        """
        ID = self.request.user.id

        members = Member.objects.filter(user_id=ID)
        
        g = []

        for i in members:
            groups = Group.objects.filter(id=i.group_id.id)
            g += groups


        return g

class NoticeDetail(generic.DetailView):
    """
        選択されたお知らせの詳細取得
    """
    model = Notice

class GroupCreate(generic.CreateView):
    template_name = 'GroupConnect/group_create.html'
    form_class = GroupCreateForm

    def get_context_data(self, **kwargs):
        """
        アイコン一覧の取得
        """
        context = super().get_context_data(**kwargs)
        context.update({
            'icon_list' : GroupIcon.objects.all()
        })
        return context

    def form_valid(self, form):
        """
        グループとメンバーの作成
        """
        icon = self.request.POST['icon']
        name = self.request.user.last_name + self.request.user.first_name
        group = form.save(commit=False)
        group.icon = icon
        group.author = name
        group.save()

        groups = Group.objects.all().latest('created_at')
        group_id = groups.id

        ID = self.request.user.id
        userid = User.objects.get(id=ID)
        groupid = Group.objects.get(id=group_id)

        Member(user_id=userid, group_id=groupid, name=name, authority=True).save()
        


        return redirect('GroupConnect:mypage')




class GroupTop(generic.DetailView):
    template_name = 'GroupConnect/group_top.html'
    model = Group

    def get_context_data(self, **kwargs):
        """
            参加メンバー一覧の取得
        """
        member_list = Member.objects.filter(group_id=self.kwargs.get('pk'))
        users = []
        for members in member_list:
            username = User.objects.filter(id=members.user_id.id)
            users += username

        context = super().get_context_data(**kwargs)
        context.update({
            'user_list' : users
        })
        return context

class GroupSet(generic.UpdateView):
    template_name = 'GroupConnect/group_setting.html'
    form_class = GroupUpdateForm
    model = Group

    def get_context_data(self, **kwargs):
        """
        参加メンバー一覧取得
        参加メンバー数取得
        (ナビバーに使う参加グループ一覧がいるかも)
        """
        ID = self.request.user.id
        members = Member.objects.filter(user_id=ID)
        member_list = Member.objects.filter(group_id=self.kwargs.get('pk'))
        membercount = Member.objects.filter(group_id=self.kwargs.get('pk')).count()
        context = super().get_context_data(**kwargs)
        context.update({
            'count' : membercount,
            'members' : member_list,
            'groups' : members
        })
        return context

    def get_success_url(self):
        return resolve_url('GroupConnect:group_setting', pk=self.kwargs['pk'])


def groupdelete(request):
    """
    グループの閉鎖
    """
    group_pk = request.POST['delete']
    Group.objects.filter(id=group_pk).delete()
    return redirect('GroupConnect:mypage')

def groupsecession(request):
    """
    グループからの脱退
    """
    ID = request.user.id
    group_pks = request.POST['secession']
    Member.objects.filter(user_id=ID, group_id=group_pks).delete()
    return redirect('GroupConnect:mypage')





class MemberList(generic.DetailView):
    template_name = 'GroupConnect/member_list.html'
    model = Group
    
    def get_context_data(self, **kwargs):
        """
            参加メンバー一覧の取得
        """
        member_list = Member.objects.filter(group_id=self.kwargs.get('pk'))
        users = []
        for members in member_list:
            username = User.objects.filter(id=members.user_id.id)
            users += username


        context = super().get_context_data(**kwargs)
        context.update({
            'user_list' : users ,
            'members' : member_list
        })
        return context

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser


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

class GroupList(generic.ListView):
    model = Group
    template_name = 'GroupConnect/grouplist.html'

    def get_context_data(self, **kwargs):

        ID = self.request.user.id
        members = Member.objects.filter(user_id=ID)

        context = super().get_context_data(**kwargs)
        context.update({
            'groups' : members
        })
        return context