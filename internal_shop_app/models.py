from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField(max_length=50)
    categoria = models.CharField(max_length=50)
    reserva = models.IntegerField(max_length=50)

    def __str__(self):
        return self.nombre
