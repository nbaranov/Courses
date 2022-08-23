#from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from accounts.models import Author


from .models import Post
from .filters import SearchNewsFilter
from .forms import PostForm

from datetime import datetime

# Create your views here.
class NewsListView(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['form'] = PostForm
        return context    

class NewsDetail(DetailView):
    model = Post
    template_name = 'news/post_detail.html'
    context_object_name = 'post'

# дженерик для создания объекта. Надо указать только имя шаблона и класс формы который мы написали в прошлом юните. Остальное он сделает за вас
class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'news/create_post.html'
    form_class = PostForm
    success_message = 'Пост успешно создан'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name = 'authors').exists()
        return context

    def form_valid(self, form):
        form.instance.author = Author.objects.get(user_id = self.request.user)   
        return super().form_valid(form)

# дженерик для редактирования объекта
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = ('news.change_post')
    template_name = 'news/create_post.html'
    form_class = PostForm
    success_message = 'Пост успешно отредактирован'
 
    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return Post.objects.get(pk=pk)
    
    def test_func(self):
        obj = self.get_object()
        return obj.author.user == self.request.user

 
# дженерик для удаления 
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = ('news.delete_post')
    template_name = 'news/delete_post.html'
    queryset = Post.objects.all()
    success_url = '/'
    success_message = 'Пост успешно удален'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author.user == self.request.user


class NewsSearchView(ListView):
    model = Post
    template_name = 'news/search_news.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['filter'] = SearchNewsFilter(self.request.GET, queryset=self.get_queryset())
        return context