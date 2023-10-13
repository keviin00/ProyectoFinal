from django.db import models
from django.contrib.auth.models import AbstractUser

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
    


