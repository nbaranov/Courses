#from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post
from .filters import SearchNewsFilter


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SearchNewsFilter(self.request.GET, queryset=self.get_queryset())
        return context
