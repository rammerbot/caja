from datetime import datetime, time

from django.db import models
from django.db.models import Q


class CajaManager(models.Manager):

    def caja_by_date(self, date):
        cajas = self.filter(created__icontains = date).order_by('-created')

        return cajas
    
    def report_by_date(self, date1, date2, sucursal):

        if len(date1) > 0 and len(date2) and len(sucursal) > 0:
            fecha1 = datetime.combine(datetime.strptime(date1,'%Y-%m-%d'), time.min)
            fecha2 = datetime.combine(datetime.strptime(date2,'%Y-%m-%d'), time.max)
            reportes = self.filter(Q(created__gte = fecha1)&Q(created__lte = fecha2), nombre_caja__sucursal__icontains = sucursal).order_by('-created')
        elif len(date1) > 0 and len(date2) > 0:
            fecha1 = datetime.combine(datetime.strptime(date1,'%Y-%m-%d'), time.min)
            fecha2 = datetime.combine(datetime.strptime(date2,'%Y-%m-%d'), time.max)
            reportes = self.filter(Q(created__gte = fecha1)&Q(created__lte = fecha2)).order_by('-created')
        elif len(sucursal) > 0:
            reportes = self.filter(nombre_caja__sucursal__icontains = sucursal)
        else:
            reportes = self.all().order_by('-created')
        return reportes