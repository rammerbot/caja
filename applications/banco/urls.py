from django.contrib import admin
from django.urls import path
from . import views

app_name = 'banco_app'
urlpatterns = [
     path('banco/', views.BancoView.as_view(), name="banco" ),
     path('dia/<pk>', views.BancoDetailView.as_view(), name="dia"),
     path('deposito/', views.DepositoView.as_view(), name="deposito" ),
     path('pago/', views.PagoView.as_view(), name="pago" ),
]
