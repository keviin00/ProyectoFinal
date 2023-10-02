from django.db import models


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
    
    
class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)  
    direccion = models.TextField()

    def __str__(self):
        return self.username
