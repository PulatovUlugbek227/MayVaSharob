from django.shortcuts import render
from. models import Drinks, Category, Product
# Create your views here.

def index (request):
    popular = Drinks.objects.all()[:6]
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {'popular': popular, 'categories': categories, 'products': products}
    return render(request, 'index.html', context)
