from django.db import models
from model_utils.models import TimeStampedModel

from applications.users.models import User
from .managers import CajaManager
# Create your models here.


class Caja(TimeStampedModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_caja = models.CharField("Sucursal-Caja", max_length=50)
    tinbet = models.DecimalField("Timbet", max_digits=10, decimal_places=2, default=0.0)
    betgana = models.DecimalField("Betgana", max_digits=10, decimal_places=2, default=0.0)
    golden = models.DecimalField("Golden", max_digits=10, decimal_places=2, default=0.0)
    soft = models.DecimalField("Soft", max_digits=10, decimal_places=2, default=0.0)
    caballos_uh1 = models.DecimalField("Caballo UH1", max_digits=10, decimal_places=2, default=0.0)
    caballos_uh2 = models.DecimalField("Caballo UH2", max_digits=10, decimal_places=2, default=0.0)
    caballos_peruvian = models.DecimalField("Caballo Peruvian", max_digits=10, decimal_places=2, default=0.0)
    mesa = models.DecimalField("Mesa", max_digits=10, decimal_places=2, default=0.0)

    """Egresos"""
    yapes = models.DecimalField("Yapes", max_digits=10, decimal_places=2, default=0.0)
    pos = models.DecimalField("POS", max_digits=10, decimal_places=2, default=0.0)
    pagos_tickets = models.DecimalField("Pago de Tickets", max_digits=10, decimal_places=2, default=0.0)
    gastos_generales = models.DecimalField("Gastos Generales", max_digits=10, decimal_places=2, default=0.0)
    
    """Ingresos"""
    cobros_tickets = models.DecimalField("Cobro de Tickets", max_digits=10, decimal_places=2, default=0.0)
    depositos = models.DecimalField("Depositos", max_digits=10, decimal_places=2, default=0.0)
    recargas = models.DecimalField("Recargas", max_digits=10, decimal_places=2, default=0.0)
    ingreso_general = models.DecimalField("Ingresos Generales", max_digits=10, decimal_places=2, default=0.0)

    """Totales"""

    efectivo = models.DecimalField("Efectivo", max_digits=10, decimal_places=2, default=0.0)
    caja_anterior = models.DecimalField("Caja Anterior", max_digits=10, decimal_places=2, default=0.0)
    caja_total = models.DecimalField("Caja Total", max_digits=10, decimal_places=2, default=0.0)
    total_sistemas = models.DecimalField("Total en Sistemas", max_digits=10, decimal_places=2, default=0.0)
    egreso_total = models.DecimalField("Egresos", max_digits=10, decimal_places=2, default=0.0)
    ingreso_total = models.DecimalField("Ingresos", max_digits=10, decimal_places=2, default=0.0)
    total_dia = models.DecimalField("Total del Dia", max_digits=10, decimal_places=2, default=0.0)
    diferencia = models.DecimalField("Diferencia", max_digits=10, decimal_places=2, default=0.0)

    """Billetes y Monedas"""

    calabaza = models.DecimalField("Calabaza", max_digits=10, decimal_places=2, default=0.0)
    guardado = models.DecimalField("Guardado", max_digits=10, decimal_places=2, default=0.0)
    centimos = models.DecimalField("Centimos", max_digits=10, decimal_places=2, default=0.0)
    rotos = models.DecimalField("Rotos", max_digits=10, decimal_places=2, default=0.0)
    cobre = models.DecimalField("Cobre", max_digits=10, decimal_places=2, default=0.0)
    cien = models.DecimalField("100", max_digits=10, decimal_places=2, default=0.0)
    cincuenta = models.DecimalField("50", max_digits=10, decimal_places=2, default=0.0)
    veinte = models.DecimalField("20", max_digits=10, decimal_places=2, default=0.0)
    diez = models.DecimalField("10", max_digits=10, decimal_places=2, default=0.0)
    cinco = models.DecimalField("5", max_digits=10, decimal_places=2, default=0.0)
    dos = models.DecimalField("2", max_digits=10, decimal_places=2, default=0.0)
    uno = models.DecimalField("1", max_digits=10, decimal_places=2, default=0.0)
    medio = models.DecimalField("0.5", max_digits=10, decimal_places=2, default=0.0)
    
    observaciones = models.TextField("Observaciones", blank=True, null=True)

    objects = CajaManager()

    class Meta:
        verbose_name = "Caja"
        verbose_name_plural = "Cajas"

    def __str__(self):
        return f"{self.id} - {self.user} - {self.nombre_caja} - {self.created}"
    