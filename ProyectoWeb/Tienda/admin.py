from django.contrib import admin
from .models import Categorias, Producto

class Admincategorias(admin.ModelAdmin):
    readonly_fields=("created","updated")
    
class Adminproducto(admin.ModelAdmin):
    readonly_fields=("created","updated")


admin.site.register(Categorias,Admincategorias)
admin.site.register(Producto,Adminproducto)