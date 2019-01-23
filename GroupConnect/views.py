from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import get_user_model
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
    LoginForm, UserCreateForm, UserUpdateForm, UserMailaddressUpdateForm, MyPasswordChangeForm,
    MyPasswordResetForm, MySetPasswordForm, DeleteUserForm, UserCreateForm
)
from .models import (
    Notice, Group, Member, User
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


'''class UserUpdate(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'GroupConnect/user_form.html'

    def get_success_url(self):
        return resolve_url('GroupConnect:user_update', pk=self.kwargs['pk'])

    context_object_name = 'rogin_user'

    def get_queryset(self):
        ID = self.request.user.id
        user = User.objects.filter(id = ID)

        return user'''

'''def UserUpdate(request, user_id):
    user = User.objects.get(id = user_id)
    return render(request, 'GroupConnect/user_form.html', {'user':user})
'''
class OnlyYouMixinTest(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.id == self.kwargs['pk'] or user.is_superuser

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

class UserTestUpdate(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'GroupConnect/user_testform.html'

    def get_success_url(self):
        return resolve_url('GroupConnect:user_testupdate', pk=self.kwargs['pk'])

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

class UserTestMailaddressUpdate(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserMailaddressUpdateForm
    template_name = 'GroupConnect/user_testmailaddress_update.html'

    def get_success_url(self):
        return resolve_url('GroupConnect:user_testmailaddress_update', pk=self.kwargs['pk'])

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




def user_delete(request):
    if request.method == 'POST':
        form = DeleteUserForm(request.POST)
        if form.is_valid(): # フォームデータの形式が正しいかどうかチェック
            if request.user.check_password(form.cleaned_data['password']): # フォームデータを取得
                user = User.objects.get(email=request.user.email)
                user.is_active = False
                user.save() # saveをしないと上のuser.is_active = Falseは反映されない
                #messages.success(request, '退会処理が完了しました。')
                return redirect('GroupConnect:top') # 他のメソッドを実行
    else:
        form = DeleteUserForm()
    return render(request, 'GroupConnect/user_delete.html', {'form': form})