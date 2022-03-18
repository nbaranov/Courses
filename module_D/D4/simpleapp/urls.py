from django.urls import path
from .views import Products, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
 
 
urlpatterns = [
    path('', Products.as_view(), name='products_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'), # Ссылка на детали товара
    path('create/', ProductCreateView.as_view(), name='product_create'), # Ссылка на создание товара
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete')
]