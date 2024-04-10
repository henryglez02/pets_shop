from django import forms

from internal_shop_app.models import Producto, Venta


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['id_producto', 'cantidad']
        widgets = {'cantidad': forms.NumberInput(
            attrs={'class': 'border border-1 rounded-md px-1'})}


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'categoria', 'reserva']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'border border-1 rounded-md px-1'}),
            'precio': forms.NumberInput(attrs={'class': 'border border-1 rounded-md px-1'}),
            'categoria': forms.TextInput(attrs={'class': 'border border-1 rounded-md px-1'}),
            'reserva': forms.NumberInput(attrs={'class': 'border border-1 rounded-md px-1'}),
        }
