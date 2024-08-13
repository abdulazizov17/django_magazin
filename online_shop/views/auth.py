from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from online_shop.forms import LoginForm,RegisterForm

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
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # password = form.cleaned_data.get('password')
            # user.is_active = True
            # user.is_superuser = True
            # user.is_staff = True
            # user.set_password(password)
            user.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = RegisterForm()

    return render(request, 'online_shop/auth/register.html')

def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('product_list')