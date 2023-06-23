from django.shortcuts import render
from .forms import Formulario
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from django.shortcuts import redirect


def Conta(request):
    Formu = Formulario()
    if request.method == "POST":
        Formu = Formulario(data=request.POST)
        if Formu.is_valid():
            nombre = request.POST.get("Nombre")
            email = request.POST.get("email")
            asunto = request.POST.get("mensaje")
            Email = EmailMessage(
                "Mensaje enviado desde app Django",
                f"Enviado por el usuario de nombre: {nombre} con dirección {email} te manda el siguiente mensaje \n {asunto}",
                "",
                ["labibliotecadelinfinito@gmail.com"],
                reply_to=[email]
            )
        try:
            Email.send()
            return redirect("http://127.0.0.1:8000/Gracias")
        except:
            return redirect("http://127.0.0.1:8000/Error")
    
    return render(request, "Contacto/Contacto", {"Formu": Formu})



def Gracias(request):
    return render(request, "Contacto/Gracias")
def Error(request):
    return render(request,"Contacto/Error")
