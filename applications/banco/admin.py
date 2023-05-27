from django.contrib import admin

from .models import Banco, Sucursal, Deposito, Pago

# Register your models here.

admin.site.register(Banco)
admin.site.register(Sucursal)
admin.site.register(Deposito)
admin.site.register(Pago)