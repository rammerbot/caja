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
        saldo_actual = Banco.objects.saldo_actual(depositos=depositos, transferencias=trasnferencias)
        context["suma_transferencias"] = suma_transferencias
        context["suma_depositos"] = suma_depositos
        context["depositos"] = depositos
        context["transferencias"] = trasnferencias
        context["saldo_actual"] = saldo_actual
        return context

class DepositoView(CreateView):
    template_name = "banco/deposito.html"
    model = Deposito
    fields = ("__all__")
    success_url=reverse_lazy("banco_app:banco")


class PagoView(CreateView):
    template_name = "banco/pago.html"
    model = Pago
    fields = ("__all__")
    success_url=reverse_lazy("banco_app:banco")

"""# Create your views here.

# Banco
class BancoView(LoginRequiredMixin, CreateView):
    template_name = 'banco/banco_cuadre.html'
    model = Banco
    fields = ('__all__')
    success_url = reverse_lazy("banco_app:banco")
    login_url = 'user_app:login'
    
# pintar el mensaje de error en el form
    def form_invalid(self, form):
        response = super().form_invalid(form)
        errors = form.errors.as_data()
        # Agrega los errores al contexto del template
        context = self.get_context_data(form=form, errors=errors)
        return self.render_to_response(context)
    #pibtar el mensaje de exito en la pantalla
    def form_valid(self, form):

        messages.success(self.request,"El registro se ha Realizado Exitosamente por favor imprima su comprovante")

        return super().form_valid(form)
    # Obtener los archivos
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bancos"] = Banco.objects.all().order_by('-fecha')[:10]
        return context
    
# crear depositos    
class DepositosView(LoginRequiredMixin, FormView):
    template_name =  'banco/depositos.html'
    form_class = DespositosForm
    success_url = reverse_lazy('banco_app:depositos')
    login_url = 'user_app:login'

    def form_invalid(self, form):
        response = super().form_invalid(form)
        errors = form.errors.as_data()
        context = self.get_context_data(form=form, errors=errors)
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        fecha = date.today()
        monto_inicial = float(self.request.POST.get('monto_inicial'))
        deposito_ingreso = float(self.request.POST.get('deposito_ingreso'))
        if Banco.objects.filter(fecha=fecha).exists():
            banco = Banco.objects.get(fecha=fecha)
            saldo_disponible = monto_inicial + deposito_ingreso

# el if del post va antes que el exist y se debe obtener el monto actual si este existe para sumarlo y si no sumar los valores iniciales unicamente   
        
        if 'recarga' in self.request.POST:
            Banco.objects.update_or_create(
                fecha = fecha,
                defaults={
                'inicio':monto_inicial, 
                'ingreso':deposito_ingreso,
                'disponible':saldo_disponible
                }
            )
            
            return self.render_to_response(context)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fecha = date.today()
        context["depositos_elviejo"] = Deposito.objects.filter(sucursal__sucursal='El Viejo', fecha__fecha=date.today()).order_by('-fecha')
        context["depositos_sport"] = Deposito.objects.filter(sucursal__sucursal='Sport', fecha__fecha=date.today()).order_by('-fecha')
        context["depositos_km40"] = Deposito.objects.filter(sucursal__sucursal='Km 40', fecha__fecha=date.today()).order_by('-fecha')

        context["total_elviejo"] = Deposito.objects.filter(sucursal__sucursal='El Viejo', fecha__fecha=date.today()).aggregate(Sum('deposito'))['deposito__sum']
        context["total_sport"] = Deposito.objects.filter(sucursal__sucursal='Sport', fecha__fecha=date.today()).aggregate(Sum('deposito'))['deposito__sum']
        context["total_km40"] = Deposito.objects.filter(sucursal__sucursal='Km 40', fecha__fecha=date.today()).aggregate(Sum('deposito'))['deposito__sum']
        return context
    
class DepositosRecargasView(TemplateView):

    template_name = "banco/depositos_recargas.html"

    def post(self, *args, **kwargs):

        inicio = float(self.request.POST.get('inicio'))
        deposito = 0.0
        Banco.objects.create(
            inicio = inicio,
            deposito = deposito,
            disponible = inicio + deposito
        )

        messages.success('El Registro se ha creado correctamente')"""
        

