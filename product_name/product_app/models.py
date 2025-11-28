from django.db import models
from django.contrib import admin
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=20, help_text='Enter product name')
    product_id = models.IntegerField(help_text='Enter product id')
    product_price = models.FloatField(help_text='Enter product price')
    product_description = models.TextField(help_text='Enter product description')
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name', 'product_id', 'product_price', 'product_description']