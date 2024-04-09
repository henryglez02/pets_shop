from typing import Any
from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField(max_length=50)
    categoria = models.CharField(max_length=50)
    reserva = models.IntegerField(max_length=50)

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    cantidad = models.IntegerField(max_length=50)
    importe = models.FloatField(max_length=50, default=0)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id_producto} - {self.cantidad}"
