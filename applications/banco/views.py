from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from applications.caja.models import Caja

# Create your views here.


class BancoView(ListView):
    template_name = 'banco/banco.html'
    context_object_name = "cajas"
    model = Caja

    def get_queryset(self):

        query = self.request.GET.get('q','')
        queryset = super(BancoView,self).get_queryset()
        if query:
            queryset = queryset.filter(user__icontains=query)
        return queryset
    
