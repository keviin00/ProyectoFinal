from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Procesador(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return self.modelo

class Memoria(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return self.modelo

class Fuente(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return self.modelo

class Motherboard(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return self.modelo
    
    




class Disco(models.Model):
    marca = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    modelo = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.marca

class Periferico(models.Model):
    marca = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    modelo = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.marca



class Usuario(models.Model):
    mail = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    nombre_completo = models.CharField(max_length=255, default='0')
    direccion = models.CharField(max_length=255, default='0')
    nombre_de_usuario = models.CharField(max_length=50, unique=True, default='0')

def __str__(self):
        return self.nombre_de_usuario

