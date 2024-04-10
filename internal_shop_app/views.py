from django.shortcuts import redirect, render

from internal_shop_app.forms import ProductoForm, VentaForm
from internal_shop_app.models import Producto, Venta

# Create your views here.


def home_view(request):
    template = "home.html"
    return render(request, template)


def tabla_view(request):
    template = "mostrar_tabla.html"
    productos = Producto.objects.all()

    return render(request, template, {"productos": productos})


def tabla_venta_view(request):
    template = "tabla_venta.html"
    ventas = Venta.objects.order_by("-id")
    for venta in ventas:
        venta.calcular_importe()
        venta.save()
    return render(request, template, {"ventas": ventas})


def agregar_producto_view(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tabla")
    else:
        template = "agregar_producto.html"
        context = {"form": ProductoForm()}
        return render(request, template, context)


def editar_producto_view(request, id_prod):
    producto = Producto.objects.get(pk=id_prod)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("tabla")
    else:
        template = "editar_producto.html"
        context = {"form": ProductoForm(instance=producto)}
        return render(request, template, context)


def eliminar_producto_view(request, id_prod):
    producto = Producto.objects.get(pk=id_prod)
    template = "eliminar_producto.html"
    context = {"producto": producto}
    return render(request, template, context)


def eliminar_producto_yes_view(request, id_prod):
    try:
        producto = Producto.objects.get(pk=id_prod)
        producto.delete()
        return redirect("tabla")
    except Exception as e:
        return render(request, "exceptions.html", {"error": str(e)})


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
    context = {"venta": venta}

    return render(request, "eliminar_venta.html", context)


def eliminar_venta_yes_view(request, id_venta):
    venta = Venta.objects.get(pk=id_venta)
    venta.delete()
    return redirect("ventas")


def editar_venta_view(request, id_venta):
    venta = Venta.objects.get(pk=id_venta)
    if request.method == "POST":
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect("ventas")
    else:
        template = "editar_venta.html"
        context = {"form": VentaForm(instance=venta)}
        return render(request, template, context)
