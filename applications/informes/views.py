from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from applications.caja.models import Caja
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden

# Create your views here.


class InformeView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, ListView):

    template_name = 'informes/informes.html'
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
    



class ListaCaja(LoginRequiredMixin,ListView):
    template_name = 'informes/fecha_caja.html'
    context_object_name = 'cajas'
    paginate_by =10
    login_url = 'users_app:login'
    
    def get_queryset(self):
        date = self.request.GET.get('date','')
        cajas = Caja.objects.caja_by_date(date)
        return cajas
    

class CajaDetailView(LoginRequiredMixin, DetailView):
    template_name = 'informes/caja_detail.html'
    model = Caja
    context_object_name = "caja"
    login_url = 'users_app:login'





