from django.shortcuts import render
from .forms import Formulario

def Conta(request):
    Formu=Formulario()
    return render(request,"Contacto/Contacto",{"Formu":Formu})

