from django.contrib import admin
from django.urls import path
from . import views

app_name = 'caja_app'
urlpatterns = [
    path('caja/', views.CajaView.as_view(), name="caja" ),
]
