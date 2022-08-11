#from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from .filters import SearchNewsFilter
from .forms import PostForm


# Create your views here.
class NewsListView(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')


class NewsDetail(DetailView):
    model = Post
    template_name = 'news/post_detail.html'
    context_object_name = 'post'



class NewsSearchView(ListView):
    model = Post
    template_name = 'news/search_news.html'
    context_object_name = 'post'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SearchNewsFilter(self.request.GET, queryset=self.get_queryset())
        return context

# дженерик для создания объекта. Надо указать только имя шаблона и класс формы который мы написали в прошлом юните. Остальное он сделает за вас
class PostCreateView(CreateView):
    template_name = 'news/create_post.html'
    form_class = PostForm

# дженерик для редактирования объекта
class PostUpdateView(UpdateView):
    template_name = 'news/create_post.html'
    form_class = PostForm
 
    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'news/delete_post.html'
    queryset = Post.objects.all()
    success_url = '/products/'