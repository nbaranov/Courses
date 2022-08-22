from django import forms

from django.contrib.auth.models import User 
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


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


class BasicSignupForm(SignupForm):
    
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user
