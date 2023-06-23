from django.contrib import admin
from django.urls import path, include
from Contacto.views import Conta, Gracias


urlpatterns = [
   path('',Conta,name="Contacto")
   ]

