from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('simpleapp.urls')), # делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py) сами автоматически подключались когда мы их добавим.
]