from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm
)
from django.contrib.auth import get_user_model
from .models import (
    Group , Signboard
)

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
            field.widget.attrs['class'] = 'form-control'

class GroupCreateForm(forms.Form):
    group_name = forms.CharField(max_length=100, required=True)
    icon = forms.ImageField()

class CreateSignboardForm(forms.ModelForm):

    class Meta:
        model = Signboard
        fields = ('title','category','text',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'