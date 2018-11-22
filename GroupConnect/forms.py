from django import forms


class MyForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='名', widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['your_name'].widget.attrs['class'] = 'form-control'
    