from django.contrib import admin
from.models import *


class categdmin(admin.ModelAdmin):
    prepopulated_fields = {'categoriesslug':('name',)}
    list_display = ['name','categoriesslug']
admin.site.register(categories,categdmin)

class prodadmin(admin.ModelAdmin):
    prepopulated_fields = {'productslug':('name',)}
    list_display = ['name','productslug','price','stock','img','availability']
    list_editable = ['price','stock','img','availability']
admin.site.register(products,prodadmin)


# admin.site.register(Cartlist)
# admin.site.register(Itemsincart)