# from django.db import models
# from .category import Category

# Create your models here.  
# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     category =models.ForeignKey(Category, on_delete=models.CASCADE)
#     image =models.ImageField(upload_to='img', height_field=None, width_field=None, max_length=None)
#     descrption =models.TextField()
#     price =models.IntegerField()

#     #Static Method
#     @ staticmethod
#     def get_category_id(get_id):    
#         if get_id:
#             return Product.objects.filter(category=get_id)
#         else:
#             return Product.objects.all()

