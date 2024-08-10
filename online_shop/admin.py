from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Catagory, Product, Comment, Order
from django.utils.html import mark_safe

# admin.site.register(Catagory)
# admin.site.register(Product)
# admin.site.register(Comment)
# admin.site.register(Order)

# admin.site.unregister(User)
admin.site.unregister(Group)



@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    search_fields = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image','raiting','category','is_very_expensive_product')
    search_fields = ('id', 'name','raiting')

    def is_very_expensive_product(self, obj):
        return obj.price >= 10_000_000

    is_very_expensive_product.boolean = True

    def image_tag(self, obj):
        if obj.image:
            return mark_safe('<img src="%s" width="50" height="50" />' % obj.image.url)
        return 'No Image'

    image_tag.short_description = 'Image'
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('id', 'user')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')

