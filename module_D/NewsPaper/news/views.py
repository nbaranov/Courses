#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class NewsListView(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news'


class NewsDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
