from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,'GestionGeneralWeb/Home')

def servicios(request):
    return render(request,'GestionGeneralWeb/Servicios')

def tienda(request):
    return render(request,'GestionGeneralWeb/Tienda')

def blog(request):
    return render(request,'GestionGeneralWeb/Blog')

def contacto(request):
    return render(request,'GestionGeneralWeb/Contacto')


