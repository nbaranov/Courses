import threading

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect

from django.contrib import messages
from accounts.models import Author

from .models import Post, Category
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
        context['news_counter'] = Post.objects.count()
        return context
    
class NewsCategoryListView(NewsListView):
    template_name = 'news/news_category_list.html'

    def get_queryset(self):
        category_id = int(self.request.GET.get("category"))
        return Post.objects.filter(category__id = category_id).order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = int(self.request.GET.get("category"))
        context['category'] = Category.objects.get(id=category_id)
        context['news_counter'] = Post.objects.filter(category__id = category_id).count()
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
    
    def send_emails(self, news):
        # получем наш html
        html_content = render_to_string( 
            'news/mail_news.html', {'news': news,}
        )
        subscribers = []
        for category in news.category.all():
            subscribers.extend(category.subscribers.all())
        for user in subscribers:
            username = user.first_name if user.first_name else user.username 
            msg = EmailMultiAlternatives(
                subject=f'«Здравствуй, {username}! Новая статья в твоём любимом разделе: {", ".join(map(str, news.category.all()))}.»',
                body=news.preview,
                from_email='poruchikrzhevsky@yandex.ru',
                to=[user.email], # это то же, что и recipients_list
            )
            msg.attach_alternative(html_content, "text/html") # добавляем html
            msg.send() # отсылаем
         
    
    def post(self, request, *args, **kwargs):
        news = Post(
            author = Author.objects.get(user__id=request.user.id),
            type = request.POST.get("type"),
            header = request.POST.get("header"),
            text = request.POST.get("text"),
            )
        news.save()
        news.category.set(request.POST.get("category"))
        news.save()
        
        tread_send_mails = threading.Thread(target=self.send_emails, args=(news,))
        tread_send_mails.start()
        
        messages.success(request, "Новость успешно добавлена")

        return redirect('post_detail', pk=news.id)

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
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post')
    template_name = 'news/delete_post.html'
    queryset = Post.objects.all()
    success_url = '/'
    success_message = 'Пост успешно удалён'    
    
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