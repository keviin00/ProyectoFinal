from itertools import product
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import Context, Template

from TiendaAPP.forms import RegistroForm
from .models import Fuente, Memoria, Motherboard, Periferico, Procesador,Disco  


def Carrito(request):
    miHTML = open(r"TiendaAPP\templates\AppTienda\Carrito.html")
    plantilla = Template(miHTML.read())
    miHTML.close()
    Context1 = Context()
    return HttpResponse(plantilla.render(Context1))


def Contacto(request):
    miHTML = open(
        r"C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Contacto.html")
    plantilla = Template(miHTML.read())
    miHTML.close()
    Context1 = Context()
    return HttpResponse(plantilla.render(Context1))


def Portada(request):
    procesadores = Procesador.objects.order_by('-precio')[:3]
    memorias = Memoria.objects.order_by('-precio')[:3]
    fuentes = Fuente.objects.order_by('-precio')[:3]
    motherboards = Motherboard.objects.order_by('-precio')[:3]
    discos = Disco.objects.order_by('-precio')[:3]
    perifericos = Periferico.objects.order_by('-precio')[:3]

    context = {
        'procesadores': procesadores,
        'memorias': memorias,
        'fuentes': fuentes,
        'motherboards': motherboards,
        'discos': discos,
        'perifericos': perifericos,
    }

    return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Portada.html', context)


def Productos(request):
    procesadores = Procesador.objects.all()
    memorias = Memoria.objects.all()
    fuentes = Fuente.objects.all()
    motherboards = Motherboard.objects.all()
    perifericos = Periferico.objects.all()  
    discos = Disco.objects.all() 

    return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Productos.html', {
        'procesadores': procesadores,
        'memorias': memorias,
        'fuentes': fuentes,
        'motherboards': motherboards,
        'perifericos': perifericos,  
        'discos': discos,
    })


def Login(request):
    miHTML = open(
        r"C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Login.html")
    plantilla = Template(miHTML.read())
    miHTML.close()
    Context1 = Context()
    return HttpResponse(plantilla.render(Context1))


def Registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Portada.html')
    else:
        form = RegistroForm()
    return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Registro.html', {'form': form})


def RecuperarPass(request):
    miHTML = open(
        r"C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\RecuperarPass.html")
    plantilla = Template(miHTML.read())
    miHTML.close()
    Context1 = Context()
    return HttpResponse(plantilla.render(Context1))


def agregar_procesador(request):
    if request.method == 'POST':
        modelo = request.POST['modelo']
        marca = request.POST['marca']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        # Obtener el valor del campo stock del formulario
        stock = request.POST['stock']

        procesador = Procesador(
            modelo=modelo, marca=marca, descripcion=descripcion, precio=precio, stock=stock)
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

        fuente = Fuente(modelo=modelo, marca=marca,
                        descripcion=descripcion, precio=precio, stock=stock)
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

        memoria = Memoria(modelo=modelo, marca=marca,
                          descripcion=descripcion, precio=precio, stock=stock)
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

        motherboard = Motherboard(
            modelo=modelo, marca=marca, descripcion=descripcion, precio=precio, stock=stock)
        motherboard.save()

        return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\exito.html')

    return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\formulario_motherboard.html')


def agregar_periferico(request):
    if request.method == 'POST':
        marca = request.POST['marca']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        modelo = request.POST['modelo']
        stock = request.POST['stock']

        periferico = Periferico(
            marca=marca, descripcion=descripcion, precio=precio, modelo=modelo, stock=stock)
        periferico.save()

        return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\exito.html')

    return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\formulario_periferico.html')

from .models import Disco  # Asegúrate de importar el modelo Disco

def agregar_disco(request):
    if request.method == 'POST':
        marca = request.POST['marca']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        modelo = request.POST['modelo']
        stock = request.POST['stock']

        disco = Disco(marca=marca, descripcion=descripcion, precio=precio, modelo=modelo, stock=stock)
        disco.save()

        return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\exito.html')
    
    return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\formulario_discos.html')


