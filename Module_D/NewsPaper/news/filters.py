from django.forms.fields import DateField
from django_filters import FilterSet
import django_filters

from accounts.models import Author
from news.models import Post


class NewsFilter (FilterSet):
    date = django_filters.DateFilter(
        field_name="create_time",
        lookup_expr="gte",
        label="Дата от",
        )
    date.field.error_messages = {'invalid' : 'Введите дату в формате ДД.ММ.ГГГГ. Например 31.12.2020'}
    date.field.widget.attrs = {'placeholder' : 'ДД.ММ.ГГГГ'}
    
    header = django_filters.CharFilter(field_name="header",
                                       lookup_expr="icontains",
                                       label="Заголовок")
    
    autorName = django_filters.TypedChoiceFilter(field_name='author',
                                                 label='Автор',)
    
    print(Author.objects.all().values_list('user__username'))
    autorName.queryset = Author.objects.all().values_list('user__username')

    
    class Meta:
        model = Post
        exclude = ['type', 'category', 'text', 'rating']
        fields = ['date', 'header', 'autorName']
        