from django.shortcuts import render, redirect,HttpResponse
from Blog.models import Categorias, post


def blog(request):
     Po=post.objects.all()
     return render(request, 'Blog/Blog', {"Po": Po})


def prueba(request, categoria_id):
    categoria = Categorias.objects.get(id=categoria_id)
    posts = post.objects.filter(categoria=categoria)
    return render(request, 'Blog/Categorias', {'categoria': categoria, 'posts': posts})

def redirectContacto(request):
     return redirect('http://127.0.0.1:8000/Contacto')


def redirectTienda(request):
     return redirect('http://127.0.0.1:8000/Tienda')


def redirectServicios(request):
     return redirect('http://127.0.0.1:8000/Servicios')


def redirectBlog(request):
     return redirect('http://127.0.0.1:8000/Blog')


def redirectPrivacidad(request):
     return redirect('http://127.0.0.1:8000/privacidad')


def redirectAviso_Legal(request):
     return redirect('http://127.0.0.1:8000/Aviso_Legal')


def redirectCookies(request):
     return redirect('http://127.0.0.1:8000/Cookie')
