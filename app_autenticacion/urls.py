from django.urls import path
from . import views

urlpatterns = [
    path('autenticacion/', views.autenticacion, name='autenticacion'),
    path('inicio/', views.inicio, name='inicio'),
    path('salir/', views.cerrar_sesion, name='cerrar_sesion'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
]