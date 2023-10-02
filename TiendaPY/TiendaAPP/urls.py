from django.contrib import admin
from django.urls import include, path

from . views import *
from TiendaAPP import views

urlpatterns = [
    path ('Portada/',views.Portada, name='Portada'),
    path ('Productos/',views.Productos,name='Productos'),
    path ('Carrito/',views.Carrito,name='Carrito'),
    path ('Contacto/',views.Contacto,name='Contacto'),
    path ('Login/',views.Login,name='Login'), 
    path ('Registro/',views.Registro,name='Registro'),
    path ('ResetPass/',views.RecuperarPass,name='RecuperarPass'),
    path('Procesador/', views.agregar_procesador, name='formulario_procesador'),
    path('Fuente/', views.agregar_fuente, name='formulario_fuente'),
    path('motherboard/', views.agregar_motherboard, name='formulario_motherboard'),
    path('MemoriaRam/', views.agregar_memoria, name='formulario_memoria'),


]