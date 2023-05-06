from django.contrib import admin
from .models import  Drinks, Product, Category
# Register your models here.
admin.site.register(Drinks)
admin.site.register(Product)
admin.site.register(Category)