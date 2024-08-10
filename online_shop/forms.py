from django import forms
from django.contrib.auth.models import User

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
from online_shop.models import Comment,Order
class CommentModelForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields='__all__'

class OrderModelForm(forms.ModelForm):

    class Meta:
        model = Order
        fields='__all__'

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    #
    # def clean_username(self):
    #     username = self.data.get('username')
    #     if not User.objects.filter(username=username).exists():
    #         raise forms.ValidationError(f'That user {username} not found')
    #     return username

