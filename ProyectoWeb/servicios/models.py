from django.db import models

class servicios(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios')
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    def __str__(self):
        return f"El servicio es: {self.titulo}"
        