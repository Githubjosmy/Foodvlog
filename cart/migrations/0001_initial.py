# Generated by Django 2.2 on 2022-10-27 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0009_auto_20221027_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=200, unique=True)),
                ('cart_added_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='items_in_cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_cart', models.IntegerField()),
                ('cart_carts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cartlist')),
                ('product_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.products')),
            ],
        ),
    ]
