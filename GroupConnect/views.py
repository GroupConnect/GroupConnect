from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)
from django.urls import reverse_lazy
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
    LoginForm, UserCreateForm, UserUpdateForm, UserMailaddressUpdateForm, MyPasswordChangeForm,
    MyPasswordResetForm, MySetPasswordForm, DeleteUserForm, UserCreateForm
)


User = get_user_model()

class Top(LoginView): #トップページ
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
        
    def form_valid(self, form):
        return render(self.request, 'GroupConnect/user_create.html', {'form': form})


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



class Mypage(generic.TemplateView): #マイページ
    template_name = 'GroupConnect/mypage.html'

    def get_context_data(self, **kwargs):
        """
        参加グループの一覧取得
        お知らせ一覧の取得。
        """
        ID = self.request.user.id
        members = Member.objects.filter(user_id=ID)

        context = super().get_context_data(**kwargs)
        context.update({
            'members': members,
            'notice_list' : Notice.objects.all()
        })
        return context


class NoticeDetail(generic.DetailView): #お知らせの詳細ページ
    """
        選択されたお知らせの詳細取得
    """
    model = Notice

class GroupCreate(generic.CreateView): #グループ作成ページ
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




class GroupTop(generic.DetailView): #グループのトップページ
    template_name = 'GroupConnect/group_top.html'
    model = Group

    def get_context_data(self, **kwargs):
        """
        参加メンバー一覧の取得
        """
        member_list = Member.objects.filter(group_id=self.kwargs.get('pk'))

        context = super().get_context_data(**kwargs)
        context.update({
            'members' : member_list
        })
        return context

class GroupSet(generic.UpdateView): #グループの設定ページ
    template_name = 'GroupConnect/group_setting.html'
    form_class = GroupUpdateForm
    model = Group

    def get_context_data(self, **kwargs):
        """
        参加メンバー一覧取得
        参加メンバー数取得
        参加グループ一覧取得
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


def mailsend(request):
    """
    メンバー招待
        メールの送信
    """
    ID = request.user.id
    email = request.POST['mailaddress']
    group_pk = request.POST['invite']
    user = User.objects.get(id=ID)
    inviteuser = User.objects.get(email=email)
    group = Group.objects.get(id=group_pk)
    current_site = get_current_site(request)
    domain = current_site.domain
    from_email = "GroupConnect@hoge.moge"
    context = {
        'protocol': request.scheme,
        'domain': domain,
        'user': user,
        'inviteuser': inviteuser,
        'group': group,
    }

    subject_template = get_template('GroupConnect/mail_template/create/invitesubject.txt')
    subject = subject_template.render(context)

    message_template = get_template('GroupConnect/mail_template/create/invitemessage.txt')
    message = message_template.render(context)

    inviteuser.email_user(subject, message, from_email)

    return redirect('GroupConnect:group_setting', group_pk)

def GroupInvite(request, **kwargs):
    """
    メンバー招待
        招待メールのリンクをクリックした後
    """
    ID = request.user.id
    user = User.objects.get(pk=kwargs.get('pk'))
    group = Group.objects.get(id=kwargs.get('id'))
    name = user.last_name + user.first_name

    if ID == user.id:
        Member(user_id=user, group_id=group, name=name, authority=False).save()
    else:
        return HttpResponseBadRequest()

    return redirect('GroupConnect:mypage')



class MemberList(generic.DetailView): #メンバー一覧ページ
    template_name = 'GroupConnect/member_list.html'
    model = Group
    
    def get_context_data(self, **kwargs):
        """
        参加メンバー一覧の取得
        """
        member_list = Member.objects.filter(group_id=self.kwargs.get('pk'))

        context = super().get_context_data(**kwargs)
        context.update({
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

class PasswordChange(PasswordChangeView):
    """パスワード変更ビュー"""
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('GroupConnect:password_change_done')
    template_name = 'GroupConnect/password_change.html'

class PasswordChangeTest(PasswordChangeView):
    """パスワード変更ビュー(テスト用)"""
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('GroupConnect:password_change_done')
    template_name = 'GroupConnect/password_change_test.html'

class PasswordChangeDone(PasswordChangeDoneView):
    """パスワード変更しました"""
    template_name = 'GroupConnect/password_change_done.html'


class PasswordReset(PasswordResetView):
    """パスワード変更用URLの送付ページ"""
    subject_template_name = 'GroupConnect/mail_template/password_reset/subject.txt'
    email_template_name = 'GroupConnect/mail_template/password_reset/message.txt'
    template_name = 'GroupConnect/password_reset_form.html'
    form_class = MyPasswordResetForm
    success_url = reverse_lazy('GroupConnect:password_reset_done')


class PasswordResetDone(PasswordResetDoneView):
    """パスワード変更用URLを送りましたページ"""
    template_name = 'GroupConnect/password_reset_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    """新パスワード入力ページ"""
    form_class = MySetPasswordForm
    success_url = reverse_lazy('GroupConnect:password_reset_complete')
    template_name = 'GroupConnect/password_reset_confirm.html'


class PasswordResetComplete(PasswordResetCompleteView):
    """新パスワード設定しましたページ"""
    template_name = 'GroupConnect/password_reset_complete.html'


class UserList(generic.ListView):
    template_name = 'GroupConnect/user_list.html'  # デフォルトUserだと、authアプリケーションのuser_list.htmlを探すため、明示的に書いておく
    model = User

class UserDataInput(generic.FormView):
    """ユーザー情報の入力

    このビューが呼ばれるのは、以下の2箇所です。
    ・初回の入力欄表示(aタグでの遷移)
    ・確認画面から戻るを押した場合(これはPOSTで飛んできます)

    初回の入力欄表示の際は、空のフォームをuser_data_input.htmlに渡し、
    戻る場合は、POSTで飛んできたフォームデータをそのままuser_data_input.htmlに渡します。

    """
    template_name = 'GroupConnect/user_data_input.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        return render(self.request, 'GroupConnect/user_data_input.html', {'form': form})

class UserDataConfirm(generic.FormView):
    """ユーザー情報の確認

    ユーザー情報入力後、「送信」を押すとこのビューが呼ばれます。(user_data_input.htmlのform action属性がこのビュー)
    データが問題なければuser_data_confirm.html(確認ページ)を、入力内容に不備があればuser_data_input.html(入力ページ)に
    フォームデータを渡します。

    """
    form_class = UserCreateForm

    def form_valid(self, form):
        return render(self.request, 'GroupConnect/user_data_confirm.html', {'form': form})

    def form_invalid(self, form):
        return render(self.request, 'GroupConnect/user_data_input.html', {'form': form})

class UserDataCreate(generic.CreateView):
    """ユーザーデータの登録ビュー。ここ以外では、CreateViewを使わないでください"""
    form_class = UserCreateForm
    success_url = reverse_lazy('GroupConnect:user_create_done')
    
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

    def form_invalid(self, form):
        """基本的にはここに飛んでこないはずです。UserDataConfrimでバリデーションは済んでるため"""
        return render(self.request, 'GroupConnect/user_data_input.html', {'form': form})


class UserDeleteView(OnlyYouMixin, generic.DeleteView):
    '''
        ユーザ退会用のビュー
        今回は再登録する際に同じメールアドレスが使えなくなることを理由に
        is_activeをfalseにするのではなくデータそのものを削除することにした   
    '''
    template_name = "GroupConnect/user_delete.html"
    success_url = reverse_lazy("GroupConnect:user_delete_done")
    model = User
    slug_field = 'pk'
    slug_url_kwarg = 'pk'

class UserDeleteDone(generic.TemplateView):
    template_name = 'GroupConnect/user_delete_done.html'
