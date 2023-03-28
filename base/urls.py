from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'base'

urlpatterns =[
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("product/", views.product, name="product"),
    path("contact/", views.contact, name="contact"),
    path("createForm/", views.createForm, name="createForm"),
    path("newsletter/", views.createNews, name="newsletter"),
    path("product/<int:product_id>/", views.product_detail, name="product_detail"),
    path("review/create/product/<int:product_id>/", views.review_create, name="review_create")
] 
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)