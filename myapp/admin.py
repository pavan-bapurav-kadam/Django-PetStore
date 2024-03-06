from django.contrib import admin
from .models import Address,Product,Order,Cart

# Register your models here.

admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)