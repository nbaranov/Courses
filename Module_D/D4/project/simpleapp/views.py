from django.shortcuts import render
from django.views.generic import ListView, DetailView # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД

from datetime import datetime

from .models import Product


#Создаем свои вьюшки

class ProductsList(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["time_now"] = datetime.utcnow()
        context["your_ads"] = None
        return context
        
 
class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'