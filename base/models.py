from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    message = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Newsletter(models.Model):
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.email
    
class ProductModel(models.Model):
    title= models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='')
    description1 = models.TextField(max_length=300)
    description2 = models.TextField(max_length=8400)
    link = models.URLField(max_length=300, default="")
    characteristic = models.CharField(max_length=150,default="")
    image = models.ImageField(upload_to='static/photos')

    def __str__(self):
        return self.title
    
class Review(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content_list = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)