# Generated by Django 2.2 on 2022-10-05 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20221005_1322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
