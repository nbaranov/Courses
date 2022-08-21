from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


from .models import Author
from .forms import UserUpdateForm


# Create your views here.
class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'accounts/profile_update.html'
    form_class = UserUpdateForm
    success_url =  reverse_lazy('profile_update') 
    success_message = 'Успешно обновлено'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        pk = self.request.user.id
        return User.objects.get(pk=pk)
