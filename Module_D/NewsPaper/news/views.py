#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from datetime import datetime


# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    queryset = Post.objects.all().order_by('id').reverse()
    
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
    