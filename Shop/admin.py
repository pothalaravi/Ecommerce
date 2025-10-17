from django.contrib import admin
from .models import Product, Category,Customer, Cart, Order

# admin login details
#  username = admin
#  password = Ravi@12345

class Categoryinfo(admin.ModelAdmin):
    list_display =["name"]

class Productinfo(admin.ModelAdmin):
    list_display =["name", "category", "price"]

class Customerinfo(admin.ModelAdmin):
    list_display =["full_name","email","mobile","password"]

class Cartinfo(admin.ModelAdmin):
    list_display =["customer", "product", "quantity"]

class Orderinfo(admin.ModelAdmin):
    list_display =["customer", "product", "quantity", "price", "address","city","pincode","total_amount","date"]

# Register your models here.

admin.site.register(Customer, Customerinfo)
admin.site.register(Product, Productinfo)
admin.site.register(Category, Categoryinfo)
admin.site.register(Cart, Cartinfo)
admin.site.register(Order, Orderinfo)