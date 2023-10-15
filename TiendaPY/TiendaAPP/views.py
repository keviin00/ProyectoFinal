from itertools import product
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import Context, Template
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


from .models import   Fuente, Memoria, Motherboard, Periferico, Procesador,Disco
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required



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

def Registro(request):
    if request.method=='GET':
            return render (request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Registro.html'
                ,{
                    'Registro' : UserCreationForm
                })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save() 
                login(request, user)
                return redirect('Login')
            except IntegrityError :
                    return render (request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Registro.html'
                ,{
                    'Registro' : UserCreationForm,
                    "error":'El Usuario Ya existe'
                })
                    
            
    return render (request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Registro.html'
                ,{
                    'Registro' : UserCreationForm,
                    "error":'Contraseñas no coinciden'
                })


def Login(request):
        if request.method == "GET":
            return render(request,r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Login.html',{
            'Inicio_de_sesion' : AuthenticationForm
        })
        else:
            user = authenticate(
                request,username=request.POST['username'],password=request.POST
                ['password'])
            if user is None:
                return render(request,r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Login.html',{
                'Inicio_de_sesion' : AuthenticationForm,
                'error' : 'Usuario o contraseña incorrecta'     
                })
            else:
                login(request, user)
                return render(request,r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Portada.html')

def CerrarSesion(request):
    logout(request)
    return render(request, r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Portada.html')


def carrito_agregar_Procesador(request, procesador_id):
    carrito = Carrito(request)
    procesador_obj = Procesador.objects.get(id=procesador_id)
    carrito.agregar(procesador_obj)
    return render(request,r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Carrito.html')

def Eliminar_Procesador(request, procesador_id):
    carrito = Carrito(request)
    Procesador = Procesador.objects.get(id+procesador_id)
    carrito.eliminar(Procesador)
    return render(request,r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Productos.html')

def restar_Procesador(request, procesador_id):
    carrito = Carrito(request)
    Procesador = Procesador.objects.get(id+procesador_id)
    carrito.restar(Procesador)
    return render(request,r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Productos.html')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request,r'C:\Users\kevin\Desktop\TiendaPY\TiendaAPP\templates\AppTienda\Productos.html')


class Carrito:
    def __init__(self,request) :
        self.request = request
        self.session = request.session
        Carrito = self.session.get("Carrito")
        if not Carrito:
            self.session['Carrito']={}
            self.Carrito = self.session['Carrito']
        else:
            self.Carrito=Carrito
    def agregar(self, Procesador):
        id = str(Procesador.id)
        if id not in self.Carrito.keys():
            self.Carrito[id]={
                "procesador_id" : Procesador.id,
                'nombre' :  Procesador.marca,
                'nombre2': Procesador.modelo,
                'stock': Procesador.stock,
                'cantidad': 1,
            }
        else:
            self.Carrito[id]["cantidad"] +=1
            self.Carrito[id]['stock'] += Procesador.stock
        self.guardar_Carrito()
    def guardar_Carrito(self):
        self.session['Carrito'] = self.Carrito
        self.session.modified = True
    def eliminar(self, Procesador):
        id = str(Procesador.id)
        if id in self.Carrito:
            del self.Carrito[id]
            self.guardar_Carrito()
    def restar(self,Procesador):
        id = str(Procesador.id)
        self.Carrito[id]["cantidad"] -=1
        self.Carrito[id]['stock'] -= Procesador.stock
        if self.Carrito[id]["cantidad"] <=0: self.eliminar(Procesador)
        self.guardar_Carrito()
    def limpiar(self):
        self.session['Carrito']={}
        self.session.modified = True

