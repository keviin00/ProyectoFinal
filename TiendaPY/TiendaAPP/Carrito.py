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
        if id not in self.Carrito.key():
            self.Carrito[id]={
                "procesador_id" : Procesador.id,
                'nombre' :  Procesador.marca,
                'nombre2': Procesador.modelo,
                'Precio': Procesador.precio,
                'cantidad': 1,
            }
        else:
            self.Carrito[id]["cantidad"] +=1
            self.Carrito[id]['Precio'] += Procesador.precio
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
        self.Carrito[id]['Precio'] -= Procesador.precio
        if self.Carrito[id]["cantidad"] <=0: self.eliminar(Procesador)
        self.guardar_Carrito()
    def limpiar(self):
        self.session['Carrito']={}
        self.session.modified = True

