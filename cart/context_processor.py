from . views import *
from . models import *


def count(request):
    item_count = 0
    if 'admin' in request.path:
        return ()
    else:
        try:
            ct = Cartlist.objects.filter(cart_id=c_id(request))
            cti = items_in_cart.objects.all().filter(cart_carts=ct[:1])
            for c in cti:
                item_count += c.quantity_cart

        except Cartlist.DoesNotExist:
            item_count = 0
    return dict(ic=item_count)

