from django.urls import  path, include
from .views import ProfileUpdateView
from .views import become_author
from .views import subscribe, unsubscribe

urlpatterns = [
    path('profile/', ProfileUpdateView.as_view(), name='profile_update'),
    path('', include('allauth.urls')),
    path('profile/become_author', become_author, name='become_author'),
    path('profile/subscribe/category/', subscribe, name='subscribe'),
    path('profile/unsubscribe/category/', unsubscribe, name='unsubscribe'),
]