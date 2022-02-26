from django.urls import  path
from .views import NewsListView, NewsDetail, NewsSearchView

urlpatterns = [
    path('', NewsListView.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
    path('search/', NewsSearchView.as_view())
]