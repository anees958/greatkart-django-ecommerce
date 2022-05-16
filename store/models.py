
from distutils.command.upload import upload
from email.mime import image
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from category.models import Category
from django.urls import reverse

class Product(models.Model):

    product_name=models.CharField(max_length=200,unique=True)
    slug =models.SlugField(max_length=200,unique=True)
    descripation=models.TextField(max_length=500,blank=True)
    price=models.IntegerField()
    images=models.ImageField(upload_to='photos/products')
    stock =models.IntegerField()
    is_avaliable=models.BooleanField(default=True)
    #foregin key
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now_add=True)

    def get_url(self):

        return reverse('product_detail',args=[self.category.slug,self.slug])
    def __str__(self) -> str:
        return self.product_name

# Create your models here.
 
class VariationManager(models.Manager):
    
    def colors(self):
        return super(VariationManager,self).filter(variation_category='color',is_active=True)
    def sizes(self):
        return super(VariationManager,self).filter(variation_category='size',is_active=True)    
variation_category_choice={
    ('color','color'),
    ('size','size'),

}
class Variation(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category=models.CharField(max_length=100, choices=variation_category_choice)
    variation_value=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    create_date=models.DateTimeField(auto_now_add=True)
    objects=VariationManager()
    def __str__(self):
        return self.variation_value