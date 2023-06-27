from django.contrib import admin
from .models import Categorias, Producto

class Admincategorias(admin.ModelAdmin):
    reandoly_fields=('create','updated')
    
class Adminproducto(admin.ModelAdmin):
    reandoly_fields=('create','updated')


admin.site.register(Categorias,Admincategorias)
admin.site.register(Producto,Adminproducto)