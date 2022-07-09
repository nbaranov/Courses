#from django.shortcuts import render
from django.views.generic import ListView, DetailView # импортируем класс получения деталей объекта

from .models import Product
from .filters import ProductFilter # импортируем недавно написанный фильтр 

class ProductList(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ads1'] = None 
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset()) # вписываем наш фильтр в контекст
        return context
 
 
# создаём представление, в котором будут детали конкретного отдельного товара
class ProductDetail(DetailView):
    model = Product # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'product.html' # название шаблона будет product.html
    context_object_name = 'product' # название объекта