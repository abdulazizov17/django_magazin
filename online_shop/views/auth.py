from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from online_shop.forms import LoginForm

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                return redirect('product_list')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request,'online_shop/auth/login.html',{'form':form})


def register_page(request):
    return render(request, 'online_shop/auth/register.html')

def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('product_list')