from django.contrib import admin

from .models import Caja, Sucursales
# Register your models here.

class CajaAdmin(admin.ModelAdmin):

    readonly_fields = ('created',)

admin.site.register(Caja,CajaAdmin)
admin.site.register(Sucursales)
