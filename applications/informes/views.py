from datetime import date

from django.db.models import Sum
from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from applications.caja.models import Caja
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from applications.banco.models import Banco, Pago, Deposito

# Create your views here.

# Informe para las cajas registradas en el sistema
class InformeCajasView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, ListView):

    template_name = 'informes/informe_cajas.html'
    context_object_name = 'reportes'
    paginate_by = 31
    login_url = 'users_app:login'
    permission_required = 'informes.informeview_caja'

    def get_queryset(self):
        date1 = self.request.GET.get('date1',"")
        date2 = self.request.GET.get('date2',"")
        sucursal = self.request.GET.get('sucursal',"")        
        cajas = Caja.objects.report_by_date(date1, date2, sucursal)
        
        return cajas
    
    def test_func(self):
        return self.request.user.username == 'Rhamer'
    
    def handle_no_permission(self):
        # Personaliza el mensaje de error y el código de estado HTTP
        return HttpResponseForbidden('Lo siento, no tienes permiso requeridos para acceder a esta página.', status=403)
    
# lista de las cajas registradas en el sistema
class ListaCaja(LoginRequiredMixin,ListView):
    template_name = 'informes/informe_caja.html'
    context_object_name = 'cajas'
    paginate_by =10
    login_url = 'users_app:login'
    
    def get_queryset(self):
        date = self.request.GET.get('date','')
        cajas = Caja.objects.caja_by_date(date)
        return cajas
    
# Detalles de las cajas registradas en el sistema
class CajaDetailView(LoginRequiredMixin, DetailView):
    template_name = 'informes/informe_caja_detail.html'
    model = Caja
    context_object_name = "caja"
    login_url = 'users_app:login'

# Vista para seleccion de tipo de informa a verificar
class InformesView(TemplateView):
    template_name = "informes/informe.html"

# Vista Para Cargar los los dias de los depositos cargados en el sistema
class BancoListView(ListView):
    template_name = "informes/informe_banco.html"
    model = Banco
    context_object_name = "bancos"
    ordering = "-created"

    def get_queryset(self):
        date1 = self.request.GET.get('date1',"")  
        bancos = Banco.objects.banco_by_date(date1)
        
        return bancos
    
    def test_func(self):
        return self.request.user.username == 'Rhamer'
# Vista para los detalles del informe del banco
class BancoDetailView(DetailView):
    template_name = "informes/informe_banco_detail.html"
    model = Banco
    context_object_name = "banco"



    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        banco = self.get_object()
        saldo_inicial = banco.saldo_inicial
        depositos = Deposito.objects.filter(created__date=banco.created.date())
        transferencias = Pago.objects.filter(created__date=banco.created.date())
        suma_depositos = Deposito.objects.filter(created__date=banco.created.date()).aggregate(sum=Sum('deposito'))['sum']
        suma_transferencias = Pago.objects.filter(created__date=banco.created.date()).aggregate(sum=Sum('pago'))['sum']
        context["depositos"] = depositos
        context["pagos"] = transferencias
        context["suma_depositos"] = suma_depositos
        context["suma_transferencias"] = suma_transferencias
        context["saldo_final"] = saldo_inicial + suma_depositos - suma_transferencias
        
        return context




