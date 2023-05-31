from django.urls import path
from GestionGeneralWeb.views import home,tienda,blog,contacto
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',home,name='Home'),
    path('Tienda',tienda, name="Tienda"),
    path('Blog',blog, name="Blog"),
    path('Contacto',contacto,name="Contacto")
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  