from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

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
    
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    procesador = models.ForeignKey(Procesador, null=True, blank=True, on_delete=models.CASCADE)
    memoria = models.ForeignKey(Memoria, null=True, blank=True, on_delete=models.CASCADE)
    fuente = models.ForeignKey(Fuente, null=True, blank=True, on_delete=models.CASCADE)
    motherboard = models.ForeignKey(Motherboard, null=True, blank=True, on_delete=models.CASCADE)
    disco = models.ForeignKey(Disco, null=True, blank=True, on_delete=models.CASCADE)
    periferico = models.ForeignKey(Periferico, null=True, blank=True, on_delete=models.CASCADE)

    def total(self):
        # Calcular el precio total del carrito
        total = 0
        for Procesador in self.Procesador.all():
            total += Procesador.precio
        for Memoria in self.Memoria.all():
            total += Memoria.precio
        for Perifericos in self.Perifericos.all():
            total += Perifericos.precio
        for Fuente in self.Fuente.all():
            total += Fuente.precio
        for Motherboard in self.Motherboard.all():
            total += Motherboard.precio
        for Disco in self.Disco.all():
            total += Disco.precio
        return total