from django.urls import  path, include
from .views import ProfileUpdateView
from .views import become_author

urlpatterns = [
    path('profile/', ProfileUpdateView.as_view(), name='profile_update'),
    path('', include('allauth.urls')),
    path('profile/become_author', become_author, name='become_author'),
]