from django.urls import path
from .views import ProductList, ProductDetail, ProductCreateView
from .views import ProductUpdateView, ProductDeleteView
 
 
urlpatterns = [
    path('', ProductList.as_view()),
    path('<int:pk>', ProductDetail.as_view(), name="product_detail"),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('create/', ProductCreateView.as_view(), name='product_create'), # Ссылка на создание товара
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete')
]