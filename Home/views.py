from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator,EmptyPage, InvalidPage


def home(request, c_slug=None):
    c_page = None
    product = None
    if c_slug != None:
        c_page = get_object_or_404(categories,categoriesslug=c_slug)
        product = products.objects.filter(category=c_page,availability=True)
    else:
        product = products.objects.all().filter(availability=True)
    cat = categories.objects.all()
    paginator = Paginator(product, '2')
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, "homepage.html", {'pr': product, 'cat': cat, 'pg': pro})

def productdetails (request,c_slug,p_slug):
    try:
        prod_details = products.objects.get(category__categoriesslug=c_slug, productslug=p_slug)
    except Exception as e:
        raise e

    return render(request, "itemdetails.html", {'pro': prod_details})

def searching(request):
    search_product=None
    search_query=None
    if 'search_item' in request.GET:
        search_query=request.GET.get('search_item')
        search_product=products.objects.all().filter(Q(name__contains=search_query)|Q(desc__contains=search_query))
    return render(request,"search.html",{'sp' : search_product,'sq': search_query})