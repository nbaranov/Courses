from django.shortcuts import render
from django.views.generic import ListView, DetailView # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД


from .models import Product
from .filters import ProductFilter


#Создаем свои вьюшки

class ProductsList(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 2
    
    
    def get_filter(self):
        return ProductFilter(self.request.GET, queryset=super().get_queryset())
    
    
    def get_queryset(self):
        return self.get_filter().qs
        

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            "your_ads" : None,
            "filter" : self.get_filter(),
        }
        
 
class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'