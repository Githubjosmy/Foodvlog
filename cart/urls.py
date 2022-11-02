from django.urls import path
from . import views

urlpatterns=[
    path('cartdetails',views.cart_details,name="cartdetailss"),
    path('add/<int:product_cart_id>/',views.add_cart,name="addtocart"),
    path('minus/<int:product_minus_id>/', views.minus_cart, name="minustocart"),
    path('delete/<int:product_delete_id>/', views.del_cart, name="deltocart"),

]