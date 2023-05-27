from datetime import date

from django.db import models

class BancoManager(models.Manager):

    def saldo_actual(self):
        dia = self.get(created__date=date.today())
        saldo_inicial = dia.saldo_inicial
        #saldo_actual =  saldo_inicial + depositos - transferencias

        return saldo_inicial

