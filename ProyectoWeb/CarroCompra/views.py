from django.shortcuts import render,redirect
from Carro import carro_Compra
from Tienda.models import Producto

def agregar(request,producto_id):
    carro=carro_Compra(request)
    producto_carro=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto_carro)
    return redirect("http://127.0.0.1:8000/Tienda")


def limpiar_carro(request):
    carro=carro_Compra(request)
    carro.limpiar_carro()
    return redirect("http://127.0.0.1:8000/Tienda")


def Eliminacion_Total(request,producto_id):
    carro=carro_Compra(request)
    producto_carro=Producto.objects.get(id=producto_id)
    carro.eliminacion_total(producto=producto_carro)
    return redirect("http://127.0.0.1:8000/Tienda")


def Restar(request,producto_id):
    carro=carro_Compra(request)
    producto_carro=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto_carro)
    return redirect("http://127.0.0.1:8000/Tienda")

