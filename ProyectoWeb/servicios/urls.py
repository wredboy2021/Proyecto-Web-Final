from django.urls import path
from servicios.views import Servicios
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('',Servicios, name="Servicios"),

]
