from django.contrib import admin
from django.urls import path
from . import views

app_name = 'informes_app'
urlpatterns = [
    path('informes/', views.InformeView.as_view(), name="informes" ),
    path('detail/<pk>', views.CajaDetailView.as_view(), name="detail" ),
    path('date/', views.ListaCaja.as_view(), name="date")
]

