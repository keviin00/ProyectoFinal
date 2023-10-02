from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import Context, Template

from TiendaAPP.forms import RegistroForm
from .models import Fuente, Memoria, Motherboard, Procesador





def Carrito(request):
    miHTML = open(r"TiendaAPP\templates\AppTienda\Carrito.html")
    plantilla = Template(miHTML.read())
    miHTML.close()
    Context1=Context()
    return  HttpResponse(plantilla.render(Context1))

def Contacto(request):
    miHTML = open(r"C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Contacto.html")
    plantilla = Template(miHTML.read())
    miHTML.close()
    Context1=Context()
    return  HttpResponse(plantilla.render(Context1))

def Portada(request):
    miHTML = open(r"C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Portada.html")
    plantilla = Template(miHTML.read())
    miHTML.close()
    Context1=Context()
    return  HttpResponse(plantilla.render(Context1))

def Productos(request):
    miHTML = open(r"C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Productos.html")
    plantilla = Template(miHTML.read())
    miHTML.close()
    Context1=Context()
    return  HttpResponse(plantilla.render(Context1))

def Login(request):
    miHTML = open(r"C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Login.html")
    plantilla = Template(miHTML.read())
    miHTML.close()
    Context1=Context()
    return  HttpResponse(plantilla.render(Context1))

def Registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a la página de inicio o a donde desees después del registro
            return redirect(r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Portada.html')
    else:
        form = RegistroForm()
    return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Registro.html', {'form': form})

def RecuperarPass(request):
    miHTML = open(r"C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\RecuperarPass.html")
    plantilla = Template(miHTML.read())
    miHTML.close()
    Context1=Context()
    return  HttpResponse(plantilla.render(Context1))

def agregar_procesador(request):
    if request.method == 'POST':
        modelo = request.POST['modelo']
        marca = request.POST['marca']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']  # Obtener el valor del campo stock del formulario

        procesador = Procesador(modelo=modelo, marca=marca, descripcion=descripcion, precio=precio, stock=stock)
        procesador.save()

        # Puedes redirigir a otra página o mostrar un mensaje de éxito
        return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\exito.html')

    return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\formulario_procesador.html')

def agregar_fuente(request):
    if request.method == 'POST':
        modelo = request.POST['modelo']
        marca = request.POST['marca']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']

        fuente = Fuente(modelo=modelo, marca=marca, descripcion=descripcion, precio=precio, stock=stock)
        fuente.save()

        return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\exito.html')

    return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\formulario_fuente.html')

def agregar_memoria(request):
    if request.method == 'POST':
        modelo = request.POST['modelo']
        marca = request.POST['marca']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']

        memoria = Memoria(modelo=modelo, marca=marca, descripcion=descripcion, precio=precio, stock=stock)
        memoria.save()

        return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\exito.html')

    return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\formulario_memoria.html')

def agregar_motherboard(request):
    if request.method == 'POST':
        modelo = request.POST['modelo']
        marca = request.POST['marca']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']

        motherboard = Motherboard(modelo=modelo, marca=marca, descripcion=descripcion, precio=precio, stock=stock)
        motherboard.save()

        return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\exito.html')

    return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\formulario_motherboard.html')
