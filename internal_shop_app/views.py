from django.shortcuts import redirect, render

from internal_shop_app.forms import CrearProducto, VentaForm
from internal_shop_app.models import Producto, Venta

# Create your views here.


def home_view(request):
    template = "home.html"
    return render(request, template)


def tabla_view(request):
    template = "mostrar_tabla.html"
    productos = Producto.objects.all()
    tipo = list(productos)
    return render(request, template, {"productos": productos, "tipo": tipo})


def tabla_venta_view(request):
    template = "tabla_venta.html"
    ventas = Venta.objects.all()
    return render(request, template, {"ventas": ventas})


def agregar_producto_view(request):
    if request.method == "POST":
        form = CrearProducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tabla")
    else:
        template = "agregar_producto.html"
        context = {"form": CrearProducto()}
        return render(request, template, context)


def editar_producto_view(request, id_prod):
    producto = Producto.objects.get(pk=id_prod)
    if request.method == "POST":
        form = CrearProducto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("tabla")
    else:
        template = "editar_producto.html"
        context = {"form": CrearProducto(instance=producto)}
        return render(request, template, context)


def eliminar_producto_view(request, id_prod):
    producto = Producto.objects.get(pk=id_prod)
    producto.delete()
    return render(request, "eliminar.html")


def agregar_venta_view(request):
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ventas")
    else:
        template = "agregar_venta.html"
        context = {"form": VentaForm()}
        return render(request, template, context)

def eliminar_venta_view(request, id_venta):
    venta = Venta.objects.get(pk=id_venta)
    venta.delete()
    return render(request, "eliminar_venta.html")