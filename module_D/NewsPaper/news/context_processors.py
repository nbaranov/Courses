from .models import Category

def categoryes(request):
    return({"categoryes" : Category.objects.all()})