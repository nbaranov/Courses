from django.db import models
from datetime import datetime


director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')
]

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    composition = models.TextField(default = "Состав не указан")
    
class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    possition = models.CharField(max_length=2, 
                                 choices=POSITIONS, 
                                 default=cashier)
    labor_contract = models.IntegerField()
    
    def get_last_name(self):
        return self.full_name.split()[0]
    
    
class Orders(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0) 
    take_away = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    products = models.ManyToManyField(Product, through='ProductOrder')
    
    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()
    
    def get_deration(self):
        if self.complete:
            return (self.time_out - self.time_in).total_seconds()//60
        else:
            return (datetime.now() - self.time_in).total_seconds()//60
    

class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    in_order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    _amount =models.IntegerField(default=1, db_column='amount')

    def product_sum(self):
        product_price = self.product.price
        return product_price * self.amount
    
    @property
    def amount(self):
        return self.amount
    
    @amount.setter
    def amount(self, value):
        self.amount = int(value) if value >= 0 else 0
        self.save
    

# Exaptle 
cap = Product(name = "Капучино 0.3", price = 99.0)
cap.save() 
cap_big = Product.objects.create(name = "Капучино 0.4", price = 109.0)

# task 2.7.1
french_fries = Product(name = "Картофель фри (стфнд.)", price = 93.0 )
french_fries.save()
french_fries_big = Product.objects.create(name = "Картофель фри (бол.)", 
                                          price = 106.0)
