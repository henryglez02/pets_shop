from django.shortcuts import redirect, render

from internal_shop_app.forms import CrearProducto
from internal_shop_app.models import Producto

# Create your views here.


def agregar_producto_view(request):

    if request.method == "GET":
        template = "agregar_producto.html"
        context = {"form": CrearProducto()}
        return render(request, template, context)

    else:
        nombre = request.POST["nombre"]
        precio = request.POST["precio"]
        reserva = request.POST["reserva"]
        categoria = request.POST["categoria"]

        producto = Producto.objects.create(
            nombre=nombre, precio=precio, reserva=reserva, categoria=categoria)
        return redirect("/angelpets/tabla")


def home_view(request):
    template = "home.html"
    return render(request, template)


def tabla_view(request):
    template = "mostrar_tabla.html"
    productos = Producto.objects.all()
    return render(request, template, {"productos": productos})


def modificar_producto_view(request, id_prod):
    return render(request, "edit.html", {"id": id_prod})


def eliminar_producto_view(request, id_prod):
    producto = Producto.objects.get(pk=id_prod)
    producto.delete()
    return render(request, "eliminar.html")


def editar_producto_view(request, id_prod):

    if request.method == "GET":
        template = "editar_producto.html"
        context = {"form": CrearProducto()}
        return render(request, template, context)

    else:
        nombre = request.POST["nombre"]
        precio = request.POST["precio"]
        reserva = request.POST["reserva"]
        categoria = request.POST["categoria"]

        producto = Producto.objects.get(pk=id_prod)
        producto.nombre = nombre
        producto.precio = precio
        producto.reserva = reserva
        producto.categoria = categoria
        producto.save()
        return redirect("tabla")
