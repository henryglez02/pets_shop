from django import forms


class CrearProducto(forms.Form):
    nombre = forms.CharField(label="Nombre")
    precio = forms.FloatField(label="Precio")
    categoria = forms.CharField(label="Categoría")
    reserva = forms.IntegerField(label="Reserva")


# TODO: henryglez02 - Terminar formulario

class CrearVenta(forms.Form):
    id_producto = forms.CharField(label="Producto")
    cantidad = forms.IntegerField(label="Cantidad")
