# models.py
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
        create_at =models.DateTimeField(auto_now=True)
        update_at = models.DateTimeField(auto_now=True)

        class Meta:
            abstract = True

class Catagory(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Catagory, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Catagories',
        db_table = 'Catagory'


    def __str__(self):
        return self.title



class Product(BaseModel):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=100)
    discription = models.TextField(null=True)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='products', null=True)
    category = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField(default=0)
    raiting = models.PositiveSmallIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero, null = True,blank=True)
    discount = models.PositiveSmallIntegerField(null=True,blank=True)



    @property
    def get_image_url(self):
        if self.image:
            return self.image.url
        return None
    # raiting = models.PositiveSmallIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero)
    # discount = models.PositiveSmallIntegerField(default=0)

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'Product'
    #
    # def get_related_products(self):
    #     return Product.objects.filter(category=self.category).exclude(id=self.id)[:5]


class Comment(BaseModel):
    user = models.ForeignKey(User,max_length=100, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    body = models.TextField()
    product = models.ForeignKey('Product', related_name='comments', on_delete=models.CASCADE)
    is_provide = models.BooleanField(default=False)
    def __str__(self):
        return f'Comment by {self.user.username} on {self.product.name}'


    class Meta:
        db_table = 'Comment'


class Order(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='order')
    quantity = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        self.product.quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)


    def __str__(self):
        return f'Order by {self.name} for {self.product.name}'

    class Meta:
        db_table = 'Order'

