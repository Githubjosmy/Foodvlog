from django.db import models
from django.template.defaultfilters import slugify

from django.urls import reverse


class categories(models.Model):
    name = models.CharField(max_length=250, unique=True)
    categoriesslug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'cat'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('prod_category', args=[self.categoriesslug])

    def __str__(self):
        return '{}'.format(self.name)


class products(models.Model):
    name = models.CharField(max_length=250, unique=True)
    productslug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField()
    img = models.ImageField(upload_to='ImageEcommerce')
    stock = models.IntegerField()
    availability = models.BooleanField()
    price = models.IntegerField()
    category = models.ForeignKey(categories, on_delete=models.CASCADE)

    #     ( on_delete=models.CASCADE) ...This is not necessary

    def get_url(self):
        return reverse('details',args=[self.category.categoriesslug,self.productslug])

    def __str__(self):
        return '{}'.format(self.name)

#
# class Cartlist(models.Model):
#     cart_id = models.CharField(max_length=200, unique=True)
#     cart_added_date = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return self.cart_id
#
#
# class Itemsincart(models.Model):
#     product_cart = models.ForeignKey(products, on_delete=models.CASCADE)
#     cart_cart = models.ForeignKey(Cartlist, on_delete=models.CASCADE)
#     quantity_cart = models.IntegerField()
#
#     def __str__(self):
#         return self.product_cart
