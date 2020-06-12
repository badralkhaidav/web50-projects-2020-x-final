from django.contrib import admin

from .models import Order, Transfer_Order
# Register your models here.

admin.site.register(Order)
admin.site.register(Transfer_Order)
