from django.forms import ModelForm
from .models import Product
 
 
# Создаём модельную форму
class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields = ['name','description', 'price', 'category', 'quantity']