from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categorias(models.Model):
    nombre=models.CharField(max_length=50)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return f"Nombre de la Categoria {self.nombre}"

class post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=200)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='Blog')
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name="post"
        verbose_name_plural="posts"
        
    def __str__(self):
        return self.name