#from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # импортируем класс получения деталей объекта

from .models import Product, Category
from .filters import ProductFilter # импортируем недавно написанный фильтр 
from .forms import ProductForm

class ProductList(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1 
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ads1'] = None 
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset()) # вписываем наш фильтр в контекст
        context['categories'] = Category.objects.all()
        context['form'] = ProductForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST) # создаём новую форму, забиваем в неё данные из POST-запроса 
 
        if form.is_valid(): # если пользователь ввёл всё правильно и нигде не накосячил, то сохраняем новый товар
            form.save()
 
        return super().get(request, *args, **kwargs)
 
# создаём представление, в котором будут детали конкретного отдельного товара
class ProductDetail(DetailView):
    model = Product # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'product/product_detail.html' # название шаблона будет product.html
    context_object_name = 'product' # название объекта


# дженерик для создания объекта. Надо указать только имя шаблона и класс формы который мы написали в прошлом юните. Остальное он сделает за вас
class ProductCreateView(CreateView):
    template_name = 'product/product_create.html'
    form_class = ProductForm


# дженерик для редактирования объекта
class ProductUpdateView(UpdateView):
    template_name = 'product/product_create.html'
    form_class = ProductForm
 
    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)

# дженерик для удаления товара
class ProductDeleteView(DeleteView):
    template_name = 'product/product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'