from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm,
    PasswordResetForm, SetPasswordForm, UserCreationForm
)
from django.contrib.auth import get_user_model
from . import models
from GroupConnect.models import Time

User = get_user_model()


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        if User.USERNAME_FIELD == 'email':
            fields = ('email',)
        else:
            fields = ('username', 'email')

        fields = ('last_name','first_name','rome_last_name','rome_first_name','email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = ''

class UserUpdateForm(forms.ModelForm):
    """ユーザー情報更新フォーム"""

    class Meta:
        model = User
        if User.USERNAME_FIELD == 'email':
            fields = ('last_name', 'first_name','rome_last_name', 'rome_first_name', 'icon', 'introduction')
        else:
            fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class UserMailaddressUpdateForm(forms.ModelForm):
    """ユーザーメールアドレス更新フォーム"""

    class Meta:
        model = User
        if User.USERNAME_FIELD == 'email':
            fields = ('plan_mail_time','new_mail_stop_time','new_mail_start_time','notice_signboard','notice_group')
        else:
            fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class MyPasswordChangeForm(PasswordChangeForm):
    """パスワード変更フォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class MyPasswordResetForm(PasswordResetForm):
    """パスワード忘れたときのフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class MySetPasswordForm(SetPasswordForm):
    """パスワード再設定用フォーム(パスワード忘れて再設定)"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class DeleteUserForm(forms.Form):
    password = forms.CharField(label='パスワード', max_length=256, widget=forms.PasswordInput())

'''--------------------------------------------'''

class UserCreateForm(UserCreationForm):
    """ユーザー登録用フォーム"""

    '''class Meta:
        model = User
        fields = (User.USERNAME_FIELD,)  # ユーザー名として扱っているフィールドだけ、作成時に入力する
    '''
    class Meta:
        model = User
        if User.USERNAME_FIELD == 'email':
            fields = ('email',)
        else:
            fields = ('username', 'email')

        fields = ('last_name','first_name','rome_last_name','rome_first_name','email')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = ''


class TimeForm(forms.ModelForm):
    plan_mail_time = forms.ModelChoiceField(models.Time.objects, to_field_name='plan_mail_time', empty_label=None, initial=0)

    class Meta:
        model = Time
        model = User
        fields = ('plan_mail_time','new_mail_stop_time','new_mail_start_time')
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'