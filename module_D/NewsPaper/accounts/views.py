from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.shortcuts import HttpResponseRedirect, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import Author
from .forms import UserUpdateForm
from news.models import Category


# Create your views here.
class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'accounts/profile_update.html'
    form_class = UserUpdateForm
    success_url =  reverse_lazy('profile_update') 
    success_message = 'Успешно обновлено'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not all([self.request.user.groups.filter(name = 'authors').exists(),
                                            Author.objects.filter(user=self.request.user).exists(),
                                           ])
        return context

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        pk = self.request.user.id
        return User.objects.get(pk=pk)




@login_required
def become_author(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        author_group.user_set.add(user)
    if not Author.objects.filter(user=user).exists():
        author = Author.objects.create(user=user, rating=0)
        author.save()
    return redirect('/add/')


@login_required
def subscribe(request):
    user_id = request.user.id
    category_id = request.GET.get('category')
    category_name = Category.objects.get(id=category_id).name
    if user_id not in Category.objects.get(id=category_id).subscribers.all():
        Category.objects.get(id=category_id).subscribers.add(user_id)
        messages.success = (request, f'Вы успешно подписаны на котегорию {category_name}')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def unsubscribe(request):
    user = request.user
    category_id = request.GET.get('category')
    category_name = Category.objects.get(id=category_id).name
    if user in Category.objects.get(id=category_id).subscribers.all():
        Category.objects.get(id=category_id).subscribers.remove(user)
        messages.success = (request, f'Вы успешно отписаны от котегории {category_name}')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))