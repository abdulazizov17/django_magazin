from django import forms
<<<<<<< HEAD

from online_shop.models import Comment, Order, Product


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'quantity']


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
=======
from online_shop.models import Comment,Order
class CommentModelForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields='__all__'

class OrderModelForm(forms.ModelForm):

    class Meta:
        model = Order
        fields='__all__'
>>>>>>> 7c1216a9553a9c89b64673b2b36b55632b600d91
