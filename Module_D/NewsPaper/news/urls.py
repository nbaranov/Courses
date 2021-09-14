from django.urls import path
from .views import IndividualNews, PostList, NewsListSearch

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', IndividualNews.as_view()),
    path('search', NewsListSearch.as_view())
]

