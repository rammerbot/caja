from django.shortcuts import render
from django.contrib import messages

from django.views.generic import TemplateView, FormView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CajaForm
from .models import Caja, Sucursales

# Create your views here.


class CajaView(LoginRequiredMixin, FormView):
    template_name = "caja/caja.html"
    form_class = CajaForm
    success_url = reverse_lazy('caja_app:caja')
    login_url = reverse_lazy('users_app:login')

    
    def post(self, request, *args, **kwargs):
        
    # Calcular la caja   
        context = self.get_context_data(**kwargs)

        if 'calcular' in self.request.POST:
            """Registro de Sistemas"""
        
            sistemas = {
                'tinbet': 0,
                'betgana': 0,
                'golden' : 0,
                'soft' : 0,
                'caballos_uh1' : 0,
                'caballos_uh2' : 0,
                'caballos_peruvian' : 0,
                'mesa' : 0
            }
        
            for key, value in sistemas.items():
                sistemas[key] = float(self.request.POST.get(key,0))
            total_sistemas = round(sum(sistemas.values()),2)
            context['resultado_sistemas']= total_sistemas or "0.0"
            
            """Registro de Egresos"""
            egresos = {
                'yapes':0,
                'pos':0,
                'pagos_tickets':0,
                'gastos_generales':0,
            }
            for key, value in egresos.items():
                egresos[key] = float(self.request.POST.get(key, 0))
            total_egresos = round(sum(egresos.values()),2)
            context['resultado_egresos'] = total_egresos or '0.0'
            
            """Registro de Ingresos"""

            ingresos = {
                'cobros_tickets':0,
                'depositos':0,
                'recargas':0,
                'ingreso_general':0
            }

            for key, value in ingresos.items():
                ingresos[key] = float(self.request.POST.get(key,0))
            total_ingresos = round(sum(ingresos.values()),2)
            context['resultado_ingresos'] = total_ingresos or '0.0'


            """Cantidad de billetes"""

            billetes = [
                ('calabaza' , 1),
                ('guardado' , 1),
                ('centimos' , 1),
                ('rotos' , 1),
                ('virtuales',1),
                ('cobre' , 1),
                ('cien' , 100),
                ('cincuenta' , 50),
                ('veinte' , 20),
                ('diez' , 10),
                ('cinco' , 5),
                ('dos' , 2),
                ('uno' , 1),
                ('medio' , 0.5)
            ]

            efectivo = 0.0
            for campo, denominacion in billetes:
                cantidad = float(self.request.POST.get(campo, 0))*denominacion
                context[f'resultado_{campo}'] = cantidad or '0.0'
                efectivo += cantidad
            context['resultado_conteo_billetes'] = efectivo

            """Total Caja"""
            
            caja_anterior = self.request.POST.get('caja_anterior')
            total_caja = round(float(efectivo) - float(caja_anterior) + float(total_egresos),2)
            context['resultado_caja_total']= total_caja or "0.0"

            """Totalizacion de cajas"""

            total_dia = round(float(total_caja) - float(total_ingresos),2)
            diferencia = round(float(total_dia) - float(total_sistemas),2)
            context['resultado_total_dia']= total_dia or "0.0"
            context['resultado_diferencia']= diferencia or "0.0"
            return self.render_to_response(context)
        
            
    # Guardar la caja Calculada

        elif 'guardar' in self.request.POST:

            """Registro de Sistemas"""
            sistemas = {
                'tinbet': 0,
                'betgana': 0,
                'golden' : 0,
                'soft' : 0,
                'caballos_uh1' : 0,
                'caballos_uh2' : 0,
                'caballos_peruvian' : 0,
                'mesa' : 0
            }
        
            for key, value in sistemas.items():
                sistemas[key] = float(self.request.POST.get(key,0))
            total_sistemas = round(sum(sistemas.values()),2)
            context['resultado_sistemas']= total_sistemas or "0.0"
                
            """Registro de Egresos"""
            egresos = {
                'yapes':0,
                'pos':0,
                'pagos_tickets':0,
                'gastos_generales':0,
            }
            for key, value in egresos.items():
                egresos[key] = float(self.request.POST.get(key, 0))
            total_egresos = round(sum(egresos.values()),2)
            context['resultado_egresos'] = total_egresos or '0.0'
            
            """Registro de Ingresos"""

            ingresos = {
                'cobros_tickets':0,
                'depositos':0,
                'recargas':0,
                'ingreso_general':0
            }

            for key, value in ingresos.items():
                ingresos[key] = float(self.request.POST.get(key,0))
            total_ingresos = round(sum(ingresos.values()),2)
            context['resultado_ingresos'] = total_ingresos or '0.0'


            """Cantidad de billetes"""

            billetes = [
                ('calabaza' , 1),
                ('guardado' , 1),
                ('centimos' , 1),
                ('rotos' , 1),
                ('virtuales',1),
                ('cobre' , 1),
                ('cien' , 100),
                ('cincuenta' , 50),
                ('veinte' , 20),
                ('diez' , 10),
                ('cinco' , 5),
                ('dos' , 2),
                ('uno' , 1),
                ('medio' , 0.5)
            ]

            efectivo = 0.0
            for campo, denominacion in billetes:
                cantidad = float(self.request.POST.get(campo, 0))*denominacion
                context[f'resultado_{campo}'] = cantidad or '0.0'
                efectivo += cantidad
            context['resultado_conteo_billetes'] = efectivo

            """Total Caja"""
        
            caja_anterior = self.request.POST.get('caja_anterior')
            total_caja = round(float(efectivo) - float(caja_anterior) + float(total_egresos),2)
            context['resultado_caja_total']= total_caja or "0.0"

            """Totalizacion de cajas"""

            total_dia = round(float(total_caja) - float(total_ingresos),2)
            diferencia = round(float(total_dia) - float(total_sistemas),2)
            context['resultado_total_dia']= total_dia or "0.0"
            context['resultado_diferencia']= diferencia or "0.0"

            """Crear Registro nuevo"""

            # Obtener los valores de los campos del formulario
            nombre_caja = request.POST.get('nombre_caja')
            tinbet = request.POST.get('tinbet')
            betgana = request.POST.get('betgana')
            golden = request.POST.get('golden')
            soft = request.POST.get('soft')
            caballos_uh1 = request.POST.get('caballos_uh1')
            caballos_uh2 = request.POST.get('caballos_uh2')
            caballos_peruvian = request.POST.get('caballos_peruvian')
            mesa = request.POST.get('mesa')

            yapes = request.POST.get('yapes')
            pos = request.POST.get('pos')
            pagos_tickets = request.POST.get('pagos_tickets')
            gastos_generales = request.POST.get('gastos_generales')

            cobros_tickets = request.POST.get('cobros_tickets')
            depositos = request.POST.get('depositos')
            recargas = request.POST.get('recargas')
            ingreso_general = request.POST.get('ingreso_general')

            caja_anterior = request.POST.get('caja_anterior')
            calabaza = request.POST.get('calabaza')
            guardado = request.POST.get('guardado')
            centimos = request.POST.get('centimos')
            rotos = request.POST.get('rotos')
            virtuales = request.POST.get('virtuales')
            cobre = request.POST.get('cobre')
            cien = round(float(request.POST.get('cien'))*100,2)
            cincuenta = round(float(request.POST.get('cincuenta'))*50,2)
            veinte = round(float(request.POST.get('veinte'))*20,2)
            diez = round(float(request.POST.get('diez'))*10,2)
            cinco = round(float(request.POST.get('cinco'))*5,2)
            dos = round(float(request.POST.get('dos'))*2,2)
            uno = round(float(request.POST.get('uno'))*1,2)
            medio = round(float(request.POST.get('medio'))*0.5,2)
          
            Caja.objects.create(
                user = self.request.user,
                nombre_caja =Sucursales.objects.get(id=int(nombre_caja)),
                tinbet = float(tinbet),
                betgana = float(betgana),
                golden = float(golden),
                soft = float(soft),
                caballos_uh1 = float(caballos_uh1),
                caballos_uh2 = float(caballos_uh2),
                caballos_peruvian = float(caballos_peruvian),
                mesa = float(mesa),
                yapes = float(yapes),
                pos = float(pos), 
                pagos_tickets = float(pagos_tickets),
                gastos_generales = float(gastos_generales),
                cobros_tickets = float(cobros_tickets),
                depositos = float(depositos),
                recargas =float(recargas),
                ingreso_general = float(ingreso_general),
                efectivo = efectivo,
                caja_anterior = float(caja_anterior),
                caja_total = total_caja,
                total_sistemas = total_sistemas,
                egreso_total = total_egresos,
                ingreso_total = total_ingresos,
                total_dia = total_dia,
                diferencia = float(diferencia),
                calabaza = float(calabaza),
                guardado = float(guardado),
                centimos = float(centimos),
                rotos = float(rotos),
                virtuales=float(virtuales),
                cobre = cobre,
                cien = cien,
                cincuenta = cincuenta,
                veinte = veinte,
                diez = diez,
                cinco = cinco,
                dos = dos, 
                uno = uno,
                medio = medio,
                observaciones = self.request.POST.get('observaciones')

            )
            messages.success(request,"El registro se ha Realizado Exitosamente por favor imprima su comprovante")
            
            return self.render_to_response(context)
