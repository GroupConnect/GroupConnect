from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm
)
from .models import User

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('last_name','first_name','rome_last_name','rome_first_name','email',
        'password')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class LoginForm(AuthenticationForm):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label