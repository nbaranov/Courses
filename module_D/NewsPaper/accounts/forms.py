from django import forms

from django.contrib.auth.models import User 

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='Логин',
        required=True,
        initial=User.username
    )
    email = forms.EmailField(
        label='Электронная почта',
        required=False,
        initial=User.email
    )
    first_name = forms.CharField(
        label='Имя',
        required=False,
        initial=User.first_name
    )
    last_name = forms.CharField(
        label='Фамилия',
        required=False,
        initial=User.last_name
    )
    
    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name']


