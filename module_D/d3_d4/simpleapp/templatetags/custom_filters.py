from django import template
 
register = template.Library()



@register.filter(name='multiply')  
def multiply(value, arg):
    if isinstance(value, float) and isinstance(arg, int): 
        return str(value * arg)
    else:
        raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}') # в случае, если кто-то неправильно воспользовался нашим тегом, выводим ошибку