from atexit import register
from django.urls import  path
from .views import ProfileUpdateView
from .views import ChangePasswordView
from .views import register   

app_name = 'accounts'
urlpatterns = [
    path('profile/', ProfileUpdateView.as_view(), name='profile_update'),
    path('password-change/', ChangePasswordView.as_view(), name='change_pass'),
    path('register/', register, name='register')
]