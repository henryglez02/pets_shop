from django.urls import path
from .views import agregar_producto_view, eliminar_producto_view, home_view, modificar_producto_view, tabla_view

urlpatterns = [
    path("home", home_view, name="home"),
    path("agregar producto", agregar_producto_view, name="agregar producto"),
    path("tabla", tabla_view, name="tabla"),
    path("tabla/editar/<int:id_prod>", modificar_producto_view, name="editar"),
    path("tabla/eliminar/<int:id_prod>", eliminar_producto_view, name="eliminar")

]