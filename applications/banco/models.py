from django.db import models
from model_utils.models import TimeStampedModel

from applications.users.models import User
from .managers import BancoManager

"""Create your models here."""

class Banco(TimeStampedModel):
    saldo_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    objects = BancoManager()

    class Meta:
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"
    
    def __str__(self):
        return str(self.created)
    
    
"""Sucursal"""
class Sucursal(TimeStampedModel):
    sucursal = models.CharField('Sucursal', max_length=30)

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
    
    def __str__(self):
        return self.sucursal
    
    
class Deposito(TimeStampedModel):

    deposito = models.DecimalField(max_digits=10, decimal_places=2)
  
    class Meta:
        verbose_name = "Deposito"
        verbose_name_plural = "Depositos"

    def __str__(self):
        return str(self.deposito)
    
class Pago(TimeStampedModel):

    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    pago = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return f"{self.sucursal} - {self.pago}"
    

