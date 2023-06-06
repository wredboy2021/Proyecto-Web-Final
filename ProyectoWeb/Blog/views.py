from django.shortcuts import render, redirect
from Blog.models import Categorias, post
# Create your views here.
def blog(request):
    Po=post.objects.all()
    return render(request,'Blog/Blog',{"Po":Po})

def prueba(request):
    return render(request, 'Blog/Categorias.html')