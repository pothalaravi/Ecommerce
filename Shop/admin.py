from django.contrib import admin
from .models import Product, Category,Customer

class Categoryinfo(admin.ModelAdmin):
    list_display =["name"]

class Productinfo(admin.ModelAdmin):
    list_display =["name", "category", "price"]

class Customerinfo(admin.ModelAdmin):
    list_display =["full_name","email","mobile","password"]

# Register your models here.

admin.site.register(Customer, Customerinfo)
admin.site.register(Product, Productinfo)
admin.site.register(Category, Categoryinfo)