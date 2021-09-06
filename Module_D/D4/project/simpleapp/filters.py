from django_filters import FilterSet
import django_filters
from .models import Category, Product

#создаем фильтр
#Попытка сдлеать нормальную форму по документации
class ProductFilter(FilterSet):
    CHOISE_CATEGORYES = Category.objects.all()
    name = django_filters.CharFilter(field_name="name",
                                             lookup_expr='icontains',
                                             label="Наименование",)
    category = django_filters.ModelChoiceFilter()
    category.label = "Категория"
    category.field_name = 'category'
    category.queryset = Category.objects.all()
    

    price_gt = django_filters.NumberFilter(field_name="price",
                                           lookup_expr="gt",
                                           label="Цена от")
    price_lt = django_filters.NumberFilter(field_name="price",
                                           lookup_expr="lt",
                                           label="Цена до")
    
    class Meta:
          model = Product
          exclude = ['quantity']
          fields = ['name', 'category', 'price_gt', 'price_lt']
          
