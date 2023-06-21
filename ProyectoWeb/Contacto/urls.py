from django.contrib import admin
from django.urls import path, include
from Contacto.views import Conta


urlpatterns = [
   path('',Conta,name="Contacto")
   ]

