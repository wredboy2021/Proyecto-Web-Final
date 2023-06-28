from django.shortcuts import render, redirect
from .models import Producto, Categorias

def Tienda(request):
    Pro=Producto.objects.all()
    return render(request,'Tienda/Tienda', {'P':Pro})

# Create your views here.
