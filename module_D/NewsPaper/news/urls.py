from django.urls import  path
from .views import NewsListView, NewsDetail

urlpatterns = [
    path('', NewsListView.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
]