from django.urls import path
from .views import NewsListView, NewsDetail, NewsSearchView


urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>', NewsDetail.as_view(), name='post_detail'),
    path('search/', NewsSearchView.as_view(), name='search_news')
]