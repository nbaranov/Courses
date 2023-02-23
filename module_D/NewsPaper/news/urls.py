from django.urls import path
from .views import NewsListView, NewsCategoryListView, NewsDetail, NewsSearchView 
from .views import PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('category/', NewsCategoryListView.as_view(), name='news_category_list'),
    path('<int:pk>', NewsDetail.as_view(), name='post_detail'),
    path('search/', NewsSearchView.as_view(), name='search_news'),
    path('add/', PostCreateView.as_view(), name='create_post'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='update_post'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
]