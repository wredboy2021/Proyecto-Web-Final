from django.urls import path
from GestionGeneralWeb.views import home,tienda,Politica,Aviso_legal,Cookies
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',home,name='Home'),
    path('Tienda',tienda, name="Tienda"),
    path('privacidad',Politica),
    path('Cookie',Cookies),
    path('Aviso_Legal',Aviso_legal)
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  