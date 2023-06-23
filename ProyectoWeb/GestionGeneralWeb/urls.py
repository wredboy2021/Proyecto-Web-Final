from django.urls import path
from GestionGeneralWeb.views import home,Politica,Aviso_legal,Cookies
from django.conf import settings
from django.conf.urls.static import static
from Contacto.views import Gracias, Error
urlpatterns = [
    path('',home,name='Home'),
    path('privacidad',Politica),
    path('Cookie',Cookies),
    path('Aviso_Legal',Aviso_legal),
    path('Gracias',Gracias),
    path('Error',Error)
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  