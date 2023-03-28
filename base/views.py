from django.shortcuts import render,redirect,get_object_or_404
from .models import Contact,Newsletter, ProductModel,Review
from .forms import NewsForm,ReviewForm

def index(request):
    context={
        "access" : True
    }
    return render(request,"html/index.html",context)

def about(request):
    context={
        "access" : True
    }
    return render(request, "html/about.html",context)

def product(request):
    context={
        "access" : True
    }
    return render(request, "html/product.html",context)

def contact(request):
    context={
        "access" : True
    }
    return render(request, "html/contact.html",context)

def createForm(request):
    if request.method == 'POST':
        user = Contact()
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.phone_number = request.POST['number']
        user.company = request.POST['company']
        user.message = request.POST['message']
        user.save()
        context = {
        'isSubmitted': True
        }
        return render(request,'html/contact.html', context)
    context = {
        'isSubmitted': False
        }
    return render(request,'html/contact.html', context)
        
# def createNews(request):
#     if request.method == 'POST':
#         news = Newsletter()
#         news.email = request.POST['email']
#         news.save()
#         context = {
#         'isSubmitted': True
#         }
#         return render(request, 'html/index.html', context)
#     context = {
#         'isSubmitted': False
#         }
#     return render(request,'html/index.html', context)

def createNews(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        news = Newsletter()
        if form.is_valid():
            news.email = form.cleaned_data['email']
            news.save()
            context = {
                'isSubmitted': True,
                "access": False
            }
            return render(request, 'html/index.html', context)
    context = {
        'isSubmitted': False
    }
    return render(request,'html/index.html', context)

def product_detail(request,product_id):
    product_list = ProductModel.objects.get(id=product_id)
    context = {'product_list':product_list}
    return render(request,'html/product_id.html',context)

def review_create(request,content_id):
    content_list = get_object_or_404(ProductModel,pk=content_id)

    if(request.method=="POST"):
        form = ReviewForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)
            content.content_list = content_list
            content.author = request.user
            content.save()
            return redirect("detail", content_id=content_list.id)
    else:
        form=ReviewForm()
        context={'context_list':content_list,"form":form}
        return render(request,'html/product_id.html',context)