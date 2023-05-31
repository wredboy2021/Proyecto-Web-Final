from django.shortcuts import render
from servicios.models import servicios

def Servicios(request):
    Sers=servicios.objects.all()
    return render(request,'servicios/Servicios',{"Sers":Sers})
