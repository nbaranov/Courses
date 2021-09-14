from django_filters import FilterSet
import django_filters

from accounts.models import Author
from news.models import Post


class NewsFilter (FilterSet):
    date = django_filters.DateFilter(field_name="create_time",
                                     lookup_expr="gte",
                                     label="Дата от")
    header = django_filters.CharFilter(field_name="header",
                                       lookup_expr="iconteins",
                                       label="Заголовок")
    autorName = django_filters.ModelChoiceFilter()
    autorName.queryset = Author.objects.all().values('user__username')
    autorName.field_name = 'author'
    autorName.label = "Автор"
    
    class Meta:
        model = Post
        exclude = ['type', 'category', 'text', 'rating']
        fields = ['date', 'header', 'autorName']
        