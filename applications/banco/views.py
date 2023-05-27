from datetime import date, timedelta
from typing import Any, Dict
from django.db.models import Sum

from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView, FormView, UpdateView, TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from .forms import DespositosForm
from applications.caja.models import Caja
from .models import Banco, Deposito, Pago

#iniciar o mostrar el dia en la caja

class BancoView(TemplateView):
    template_name = "banco/banco.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if Banco.objects.filter(created__date=date.today()).exists():
            dia_detalle = Banco.objects.get(created__date=date.today())
            respuesta = "para ingresar al dia"
            context["dia_detalle"] = dia_detalle
        else:
            respuesta = "crear el dia"

        context["respuesta"] = respuesta
    
        return context

# Detalles del banco, saldos, depositos y transferencias
class BancoDetailView(DetailView):
    template_name = "banco/banco_detail.html"
    model = Banco
    context_object_name = "dia"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        depositos = Deposito.objects.filter(created__date=date.today())
        trasnferencias = Pago.objects.filter(created__date=date.today()).order_by('sucursal')
        suma_depositos = Deposito.objects.filter(created__date=date.today()).aggregate(sum=Sum('deposito'))['sum']
        suma_transferencias = Pago.objects.filter(created__date=date.today()).aggregate(sum=Sum('pago'))['sum']
        saldo_inicial = Banco.objects.saldo_actual()
        context["suma_transferencias"] = suma_transferencias
        context["suma_depositos"] = suma_depositos
        context["depositos"] = depositos
        context["transferencias"] = trasnferencias
        context["saldo_inicial"] = saldo_inicial
        if suma_depositos and suma_transferencias:
            context["saldo_disponible"] = suma_depositos + saldo_inicial - suma_transferencias
        elif suma_transferencias:
            context["saldo_disponible"] = saldo_inicial - suma_transferencias
        elif suma_depositos:
            context["saldo_disponible"] = saldo_inicial + suma_depositos
        else:
            context["saldo_disponible"] = saldo_inicial
            
        return context
    
# Cargar depositos realizados durante el dia
class DepositoView(CreateView):
    template_name = "banco/deposito.html"
    model = Deposito
    fields = ("__all__")
    success_url=reverse_lazy("banco_app:banco")

# Cargar Transferencias realizadas durante el dia
class PagoView(CreateView):
    template_name = "banco/pago.html"
    model = Pago
    fields = ("__all__")
    success_url=reverse_lazy("banco_app:banco")

# Crear Dia de trabajo en el sistema
class CreateDay(CreateView):
    template_name = "banco/banco_create.html"
    model = Banco
    fields = ("__all__")
    success_url = reverse_lazy("banco_app:banco")
