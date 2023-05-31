from django.shortcuts import render,HttpResponse
from servicios.models import servicios

def home(request):
    return render(request,'GestionGeneralWeb/Home')


def tienda(request):
    return render(request,'GestionGeneralWeb/Tienda')

def blog(request):
    return render(request,'GestionGeneralWeb/Blog')

def contacto(request):
    return render(request,'GestionGeneralWeb/Contacto')


