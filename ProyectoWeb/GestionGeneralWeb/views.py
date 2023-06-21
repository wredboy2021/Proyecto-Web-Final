from django.shortcuts import render,HttpResponse
from servicios.models import servicios

def home(request):
    return render(request,'GestionGeneralWeb/Home')


def tienda(request):
    return render(request,'GestionGeneralWeb/Tienda')




def Politica(request):
    return render(request, 'GestionGeneralWeb/Politica_de_Privacidad')

def Aviso_legal(request):
    return render(request,'GestionGeneralWeb/Aviso_legal')

def Cookies(request):
    return render(request,'GestionGeneralWeb/Cookies')
