from django.contrib import admin
from .models import Categorias, post


class adminCategoria(admin.ModelAdmin):
    readonly_fields=("create","update")

class adminPost(admin.ModelAdmin):
    readonly_fields=('create','update')

admin.site.register(Categorias,adminCategoria)
admin.site.register(post,adminPost)
