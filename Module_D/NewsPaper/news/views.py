#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from .filters import NewsFilter
from datetime import datetime


# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    queryset = Post.objects.all().order_by('id').reverse()
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["time_now"] = datetime.utcnow()
        return context

    
class IndividualNews(DetailView):
    model = Post
    template_name = 'individual_news.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post=self.get_object()).reverse()
        return context
    
# создаем новую вьюшку для страницы поиска с фильтром
class NewsListSearch(ListView):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'news_search'
    queryset = Post.objects.all().order_by('id').reverse()
    paginate_by = 5
    
    
    def get_filter(self):
        return NewsFilter(self.request.GET, queryset=super().get_queryset()).qs


    def get_queryset(self):
        return self.get_filter()

    
    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            "time_now" : datetime.utcnow(),
            "filter" : self.get_filter()
        }