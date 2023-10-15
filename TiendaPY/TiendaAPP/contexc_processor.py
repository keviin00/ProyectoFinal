def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if request.session["Carrito"]:
            for key,value in request.session["Carrito"].item():
                total+= int(value["Precio"])
        return{"total_carrito":total}
