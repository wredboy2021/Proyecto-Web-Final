from django.contrib import admin
from .models import servicios

class admin_servicio(admin.ModelAdmin):
    readonly_fields=("create","update")

admin.site.register(servicios, admin_servicio)
# Register your models here.
