from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homes'),
    path('<slug:c_slug>/',views.home,name='prod_category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.productdetails,name="details"),
    path('search', views.searching, name="searches"),
             ]
