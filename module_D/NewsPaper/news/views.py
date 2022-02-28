#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from .filters import SearchNewsFilter

from datetime import datetime

# Create your views here.
class NewsListView(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class NewsSearchView(ListView):
    model = Post
    template_name = 'search_news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['filter'] = SearchNewsFilter(self.request.GET, queryset=self.get_queryset())
        return context
