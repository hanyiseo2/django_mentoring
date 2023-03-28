from django.contrib import admin
from .models import Contact,Newsletter,ProductModel,Review
# Register your models here.

admin.site.register(Contact)
admin.site.register(Newsletter)
admin.site.register(ProductModel)
admin.site.register(Review)