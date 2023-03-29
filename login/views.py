from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from login.forms import UserForm
# Create your views here.

# def logout(request):
#     auth_logout(request)
#     return redirect('index')

def register(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request,user)
    else:
        form=UserForm()
    return render(request, 'register.html',{'form':form})

# def login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request,user)
#             return redirect('index')
#         # username = request.POST['username']
#         # password = request.POST['password']
#         # user = authenticate(request, username=username, password=password)
#         # if user is not None:
#         #     auth_login(request,user)
#         #     # isLogin = True
#         #     return redirect('index')
#         #     # return render(request,'../base/index.html',{isLogin:isLogin})
#         else:
#             error_message = 'Invalid credentials. Please try again.'
#             return render(request,"login.html", {'error_message': error_message})
        
#     else:
#         form= AuthenticationForm()
#         return render(request, 'login.html')
    