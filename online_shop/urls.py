from django.urls import path
from django.contrib import admin

from online_shop.views import views
from online_shop.views import auth
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('catagory/<slug:category_slug>/', views.product_list, name='category_detail_id'),
    # path('catagories/', views.product_list, name='catagories'),
    path('product-detail/<int:product_id>', views.product_detail, name='product_detail'),
    path('add-comment/<int:product_id>/', views.add_comment, name='add_comment'),
    path('add-order/<int:product_id>/', views.add_order, name='add_order'),
    path('add-product/', views.add_product, name='add_product'),
    path('delete-product/<int:product_id>', views.delete_product, name='delete_product'),
    path('edit-product/<int:product_id>', views.edit_product, name='edit_product'),
    path('product_detail/<int:product_id>', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/add-comment',views.add_comment,name = 'add_comment'),
    path('product/<int:product_id>/add_order',views.add_order,name ='add_order'),


# authontifacation

    path('login-page/' , auth.login_page, name = 'login_page'),
    path('register-page/', auth.register_page, name='register_page'),
    path('logout_page/',auth.login_page, name='logout_page')

]
