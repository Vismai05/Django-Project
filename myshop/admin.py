from django.contrib import admin
from .models import myprd, prdlist, contact, Order, orderstatus
# Register your models here.

admin.site.register(myprd)
admin.site.register(prdlist)
admin.site.register(contact)

class orderadmin(admin.ModelAdmin):
    list_display = ['order_id','name','phone','email']
    search_fields = ('order_id',)
admin.site.register(Order,orderadmin)

class statusadmin(admin.ModelAdmin):
    list_display = ['order_id','status']
    search_fields = ('order_id',)
admin.site.register(orderstatus,statusadmin)