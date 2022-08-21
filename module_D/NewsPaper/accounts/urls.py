from django.urls import  path, include
from .views import ProfileUpdateView

urlpatterns = [
    path('profile/', ProfileUpdateView.as_view(), name='profile_update'),
    path('', include('allauth.urls'))
]