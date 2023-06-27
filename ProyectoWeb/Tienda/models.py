from django.db import models


class Categorias(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    categoria=models.ForeignKey(Categorias, on_delete=models.CASCADE)
    precio=models.FloatField()
    imagen=models.ImageField(upload_to='Tienda', null=True,blank=True)
    disponibilidad=models.BooleanField(default=True)
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
    def __str__(self):
        return self.nombre
    