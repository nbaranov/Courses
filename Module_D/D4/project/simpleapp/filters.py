from django_filters import FilterSet
from .models import Product

#создаем фильтр
class ProductFilter(FilterSet):
    class Meta:
        model = Product
        field = ('name', 'category', 'price')