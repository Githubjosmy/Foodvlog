# Generated by Django 2.2 on 2022-10-27 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_auto_20221027_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemsincart',
            name='cart_cart',
        ),
        migrations.RemoveField(
            model_name='itemsincart',
            name='product_cart',
        ),
        migrations.DeleteModel(
            name='cartlist',
        ),
        migrations.DeleteModel(
            name='itemsincart',
        ),
    ]
