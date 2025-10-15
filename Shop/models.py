from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    image =models.ImageField(upload_to='img', height_field=None, width_field=None, max_length=None)
    descrption =models.TextField()
    price =models.IntegerField()

    #Static Method
    @ staticmethod
    def get_category_id(get_id):    
        if get_id:
            return Product.objects.filter(category_id=get_id)
        else:
            return Product.objects.all()
        
    def __str__(self):
        return self.name


#Sign up

class Customer(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    mobile =models.CharField(max_length=15)
    password =models.CharField(max_length=128)

    def __str__(self):
        return self.full_name



# Checking if email is existing or not
    def isexist(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.customer.full_name} - {self.product.name}"
    def total_price(self):
        return self.product.price * self.quantity





