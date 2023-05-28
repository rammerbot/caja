from django.contrib import admin
from django.urls import path
from . import views

app_name = 'informes_app'
urlpatterns = [
    path('informes', views.InformesView.as_view(), name="informes"),
    path('informe_cajas/', views.InformeCajasView.as_view(), name="informe_cajas" ),
    path('detail/<pk>', views.CajaDetailView.as_view(), name="detail" ),
    path('date/', views.ListaCaja.as_view(), name="date"),
    path('informe_bancos', views.BancoListView.as_view(), name="informe_bancos"),
    path('banco_detail/<pk>', views.BancoDetailView.as_view(), name="banco_detail")
]

