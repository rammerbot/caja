from django.contrib import admin
from django.urls import path
from . import views

app_name = 'banco_app'
urlpatterns = [
    path('banco/', views.BancoView.as_view(), name="banco" ),
]
