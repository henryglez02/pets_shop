from django import forms

from internal_shop_app.models import Producto, Venta


# class CrearProducto(forms.Form):
#     nombre = forms.CharField(label="Nombre")
#     precio = forms.FloatField(label="Precio")
#     categoria = forms.CharField(label="Categoría")
#     reserva = forms.IntegerField(label="Reserva")

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['id_producto', 'cantidad']


class CrearProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'categoria', 'reserva']
