from django_filters import FilterSet
from .models import Product

#создаем фильтр
class ProductFilter(FilterSet):
    class Meta:
        model = Product
        exclude = ['quantity']
        # interface = ('relay.Node',)
        fields = {'name' : ['contains'], 
                #   'category' : [], 
                  'price' : ['lt']}