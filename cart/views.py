from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from Home . models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def cart_details(request, total=0, count=0, c_adds=None):

    try:
        ct = Cartlist.objects.get(cart_id=c_id(request))
        c_adds = items_in_cart.objects.filter(cart_carts=ct, active=True)
        for i in c_adds:
            total += (i.product_cart.price * i.quantity_cart)
            count += i.quantity_cart


    except ObjectDoesNotExist:
        pass
    return render(request, "cart.html", {'ci': c_adds, 'tot': total, 'co': count})

def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id

def add_cart(request,product_cart_id):
    prod_cart = products.objects.get(id=product_cart_id)

    try:
        ct = Cartlist.objects.get(cart_id=c_id(request))
    except Cartlist.DoesNotExist:
        ct = Cartlist.objects.create(cart_id=c_id(request))
        ct.save()

    try:
        c_items = items_in_cart.objects.get(product_cart=prod_cart,cart_carts=ct)
        if c_items.quantity_cart < c_items.product_cart.stock:
            c_items.quantity_cart += 1
            c_items.save()
    except items_in_cart.DoesNotExist:
         c_items = items_in_cart.objects.create(product_cart=prod_cart, quantity_cart=1, cart_carts=ct)
         c_items.save()
    return redirect("cartdetailss")



def minus_cart(request,product_minus_id):
    ct = Cartlist.objects.get(cart_id=c_id(request))
    ct_minus_product = get_object_or_404(products,id=product_minus_id)
    c_items = items_in_cart.objects.get(product_cart=ct_minus_product,cart_carts=ct)
    if c_items.quantity_cart > 1:
        c_items.quantity_cart-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect("cartdetailss")


def del_cart(request,product_delete_id):
    ct = Cartlist.objects.get(cart_id=c_id(request))
    ct_minus_product = get_object_or_404(products, id=product_delete_id)
    c_items = items_in_cart.objects.get(product_cart=ct_minus_product, cart_carts=ct)
    c_items.delete()
    return redirect("cartdetailss")


