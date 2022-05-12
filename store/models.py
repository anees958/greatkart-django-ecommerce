
from distutils.command.upload import upload
from email.mime import image
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
