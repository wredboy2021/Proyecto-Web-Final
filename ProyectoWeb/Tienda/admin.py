from django.contrib import admin
from .models import Categorias, Producto

class Admincategorias(admin.ModelAdmin):
    reandoly_fields=('create','update')
    
class Adminproducto(admin.ModelAdmin):
    reandoly_fields=('create','update')


admin.site.register(Categorias,Admincategorias)
admin.site.register(Producto,Adminproducto)