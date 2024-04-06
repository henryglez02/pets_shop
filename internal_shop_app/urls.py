from django.urls import path
from .views import agregar_producto_view, agregar_venta_view, editar_producto_view, eliminar_producto_view, eliminar_venta_view, home_view, tabla_venta_view,  tabla_view

urlpatterns = [
    path("home", home_view, name="home"),
    path("agregar producto", agregar_producto_view, name="agregar producto"),
    path("tabla", tabla_view, name="tabla"),
    path("ventas", tabla_venta_view, name="ventas"),
    path("tabla/editar/<int:id_prod>", editar_producto_view, name="editar"),
    path("tabla/eliminar/<int:id_prod>",
         eliminar_producto_view, name="eliminar"),
    path("agregar venta", agregar_venta_view, name="agregar venta"),
    path("tabla/eliminar venta/<int:id_venta>",
         eliminar_venta_view, name="eliminar venta"),


]
