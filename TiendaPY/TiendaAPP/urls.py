from django.contrib import admin
from django.urls import include, path

from . views import *
from TiendaAPP import views

urlpatterns = [
    path ("Inicio",views.Portada, name='Portada'),
    path ('Productos/',views.Productos,name='Productos'),
    path ('Carrito/',views.Carrito,name='Carrito'),
    path ('Contacto/',views.Contacto,name='Contacto'),
    path ('Login/',views.Login,name='Login'), 
    path ('Registro/',views.Registro,name='Registro'),
    path ('ResetPass/',views.RecuperarPass,name='RecuperarPass'),
    path('Agregar_Procesador/', views.agregar_procesador, name='formulario_procesador'),
    path('Agregar_Fuente/', views.agregar_fuente, name='formulario_fuente'),
    path('Agregar_motherboard/', views.agregar_motherboard, name='formulario_motherboard'),
    path('Agregar_MemoriaRam/', views.agregar_memoria, name='formulario_memoria'),
    path('Agregar_Perifericos/', views.agregar_periferico, name='formulario_periferico'),
    path('Agregar_Discos/', views.agregar_disco, name='formulario_discos'),       
]