from typing import Optional

<<<<<<< HEAD
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from online_shop.forms import CommentModelForm, OrderModelForm, ProductModelForm
from online_shop.models import Catagory, Product, Comment
=======
from django.shortcuts import render,redirect,get_object_or_404

from online_shop.models import Catagory, Product,Comment
from online_shop.forms import CommentModelForm,OrderModelForm
>>>>>>> 7c1216a9553a9c89b64673b2b36b55632b600d91


def product_list(request, catagory_id: Optional[int] = None):
    catagories = Catagory.objects.all().order_by(('id'))
    if catagory_id:
        products = Product.objects.filter(category=catagory_id)
    else:
        products = Product.objects.all()
    context = {'products': products,
<<<<<<< HEAD
               'catagories': catagories
=======
               'catagories':catagories
>>>>>>> 7c1216a9553a9c89b64673b2b36b55632b600d91

               }

    return render(request, 'online_shop/home.html', context)


def product_detail(request, product_id):
<<<<<<< HEAD
    comments = Comment.objects.filter(product=product_id, is_provide=True).order_by('-id')
    product = Product.objects.get(id=product_id)
    context = {'product': product,
               'comments': comments
               }
    return render(request, 'online_shop/detail.html', context)


=======
    comments = Comment.objects.filter(product=product_id,is_provide=True).order_by('-id')
    product = Product.objects.get(id=product_id)
    context = {'product': product,
               'comments':comments
               }
    return render(request, 'online_shop/detail.html', context)

>>>>>>> 7c1216a9553a9c89b64673b2b36b55632b600d91
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

<<<<<<< HEAD
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
    return render(request,'online_shop/edit-product.html',{'form':form})
=======
def add_comment(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    if request.method =='POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product=product
            comment.save()
            return redirect('product_detail',product_id)
    else:
        form = CommentModelForm()

    return render(request,'online_shop/detail.html',{'form':form})

def add_order(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    if request.method=='POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            product.quantity -= int(form.data.get('quantity'))
            order = form.save(commit=False)
            order.product = product
            order.save()
            if order.quantity < product.quantity:
                return render(request, 'online_shop/detail.html', {'form': form, 'product': product, })
            order.save()
            return redirect('product_detail',product_id)
    else:
        form= OrderModelForm()
    contex = {'form':form,'product':product}
    return render(request,'online_shop/detail.html',contex)

>>>>>>> 7c1216a9553a9c89b64673b2b36b55632b600d91
