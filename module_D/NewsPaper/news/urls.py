from django.urls import path
from .views import NewsListView, NewsDetail


urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>', NewsDetail.as_view(), name='post_detail')
]