from django.forms import ModelForm, BooleanField
from .models import Product
 
 
# Создаём модельную форму
class ProductForm(ModelForm):
    check_box = BooleanField(label='Ало, Галочка!') # добавляем галочку или же true-false поле
    
    class Meta:
        model = Product
        fields = ['name','description', 'price', 'category', 'quantity']