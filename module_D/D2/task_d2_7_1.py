# Example from unit D2.7
cap = Product(name="Капучино 0.3", price=99.0)
cap.save()
cap_big = Product.objects.create(name="Капучино 0.4", price=109.0)

# Task D2.7.1
fries_std = Product(name="Картофель фри (стандарт)", price=93.0)
fries_std.save()
fries_big = Product.objects.create(name="Картофель фри (большой)", price=106)
