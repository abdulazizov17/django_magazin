from typing import Optional
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from online_shop.forms import CommentModelForm, OrderModelForm, ProductModelForm
from online_shop.models import Catagory, Product, Comment
from django.shortcuts import render,redirect,get_object_or_404

from online_shop.models import Catagory, Product,Comment
from online_shop.forms import CommentModelForm,OrderModelForm
from django.db.models import Q

def product_list(request, catagory_slug: Optional[str] = None):
    catagories = Catagory.objects.all().order_by(('id'))
    search = request.GET.get('q')
    filter_type = request.GET.get('filter','')
    if catagory_slug:
        if filter_type == 'expensive':
              products = Product.objects.filter(category__slug=catagory_slug).order_by('-price')
        elif filter_type == 'cheap':
            products = Product.objects.filter(category__slug=catagory_slug).order_by('price')
        elif filter_type == 'rating':
            products = Product.objects.filter(Q(category__slug=catagory_slug) & Q(rating__gte=4)).order_by('-price')
        else:
            products = Product.objects.filter(category__slug=catagory_slug)

    else:
        if filter_type == 'expensive':
              products = Product.objects.all().order_by('-price')
        elif filter_type == 'cheap':
            products = Product.objects.all().order_by('price')
        elif filter_type == 'rating':
            products = Product.objects.filter(Q(rating__gte=4)).order_by('-rating')
        else:
            products = Product.objects.all()


    if search:
        products = products.filter(Q(name__icontains=search))

    context = {'products': products,
               'catagories': catagories

               }

    return render(request, 'online_shop/home.html', context)


def product_detail(request, product_id):
    catagories = Catagory.objects.all()
    product = Product.objects.get(id=product_id)
    min_price = product.price*0.2
    max_price = product.price*1.8
    simmilar_products = Product.objects.filter(category=product.category,price__range=[min_price,max_price]).exclude(id=product_id)
    comments = Comment.objects.filter(product=product_id, is_provide=True).order_by('-id')
    context = {'product': product,
               'comments': comments,
               'catagories':catagories,
               'simmilar_products':simmilar_products
               }
    return render(request, 'online_shop/detail.html', context)


# def add_comment(request,product_id):
#     product = get_object_or_404(Product,id = product_id)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email ')
#         body = request.POST.get('body')
#         commnet = Comment(name=name,email=email,body=body)
#         commnet.product=product
#         commnet.save()
#         return redirect('product_detail',product_id )
#
#     else:
#         pass
#     return render(request,'online_shop/detail.html')

def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', product_id)
    else:
        form = CommentModelForm()
    contex = {
        'form': form
    }

    return render(request, 'online_shop/detail.html', contex)


def add_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = OrderModelForm()
    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            if product.quantity >= int(form.cleaned_data['quantity']):
                product.quantity -= int(form.cleaned_data['quantity'])
                product.save()
                new_product = form.save(commit=False)
                new_product.product = product
                new_product.save()
                messages.add_message(
                    request,
                    level=messages.SUCCESS,
                    message='Your order is successfully saved'
                )
                return redirect('product_detail', product_id)
            else:
                messages.add_message(
                    request,
                    level=messages.ERROR,
                    message='Yuor order is not available'
                )
    contex = {
        'form': form,
        'product': product
    }
    return render(request, 'online_shop/detail.html', contex)


@login_required
def add_product(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    contex = {
        'form': form
    }
    return render(request, 'online_shop/add-product.html', contex)

def delete_product(request,product_id):
    product = get_object_or_404(Product,id = product_id )
    if product:
        product.delete()
        return redirect('product_list')

def edit_product(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    form = ProductModelForm(instance=product)
    if request.method == 'POST':
        form = ProductModelForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail',product_id)

    return render(request, 'online_shop/edit-product.html', {'form':form})

