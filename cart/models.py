from Home.models import *
from django.db import models

class Cartlist(models.Model):
    cart_id = models.CharField(max_length=200, unique=True)
    cart_added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class items_in_cart(models.Model):
    product_cart = models.ForeignKey(products, on_delete=models.CASCADE)
    cart_carts = models.ForeignKey(Cartlist, on_delete=models.CASCADE)
    quantity_cart = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product_cart

    def totals(self):
        return self.product_cart.price * self.quantity_cart

    def left(self):
        return self.product_cart.stock - self.quantity_cart