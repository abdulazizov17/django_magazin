# Generated by Django 5.0.7 on 2024-08-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0008_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='raiting',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Zero'), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], default=0, null=True),
        ),
    ]
