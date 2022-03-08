
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Author
from .forms import UserUpdateForm


# Create your views here.
class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView, ):
    template_name = 'accounts/profile_update.html'
    form_class = UserUpdateForm
    success_url =  reverse_lazy('accounts:profile_update') 
    success_message = 'Успешно обновлено'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        pk = self.request.user.id
        return User.objects.get(pk=pk)

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_message = "Пароль успешно изменён."
    success_url = reverse_lazy('accounts:profile_update')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            Author.objects.create(user=user)
            return redirect('accounts:profile_update')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})