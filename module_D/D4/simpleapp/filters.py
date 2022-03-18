from django_filters import FilterSet, filters # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Product, Category
 
 
# создаём фильтр
class ProductFilter(FilterSet):
    name = filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Имя содержит'
    )
    price_min = filters.NumberFilter(
        field_name='price',
        lookup_expr='gt',
        label='Цена от',
    )
    price_max = filters.NumberFilter(
        field_name='price',
        lookup_expr='lt',
        label='Цена до',
    )
    category = filters.ModelChoiceFilter(
        field_name='category',
        label='Категория',
        queryset=Category.objects.all()
    )
    class Meta:
        model = Product
        exclude = ['quantity', 'price', 'category', 'name']
