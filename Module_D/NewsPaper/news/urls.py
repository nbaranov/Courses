from django.urls import path
from .views import IndividualNews, PostList

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', IndividualNews.as_view())
]
