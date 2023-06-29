
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Blog.views import blog, prueba, redirectBlog, redirectContacto, redirectServicios, redirectTienda, redirectAviso_Legal, redirectCookies, redirectPrivacidad

urlpatterns = [
path('',blog,name='Blog'),
path('/categorias/<categoria_id>/',prueba,name='categorias'),
path('/categorias/1/Blog', redirectBlog),
path("/categorias/2/Blog", redirectBlog),
path("/categorias/3/Blog", redirectBlog),
path('/categorias/1/Contacto', redirectContacto),
path("/categorias/2/Contacto", redirectContacto),
path("/categorias/3/Contacto", redirectContacto),
path('/categorias/1/Servicios', redirectServicios),
path("/categorias/2/Servicios", redirectServicios),
path("/categorias/3/Servicios", redirectServicios),
path('/categorias/1/privacidad', redirectPrivacidad),
path("/categorias/2/privacidad", redirectPrivacidad),
path("/categorias/3/privacidad", redirectPrivacidad),
path('/categorias/1/Aviso_Legal', redirectAviso_Legal),
path("/categorias/2/Aviso_Legal", redirectAviso_Legal),
path("/categorias/3/Aviso_Legal", redirectAviso_Legal),
path('/categorias/1/Cookie', redirectCookies),
path("/categorias/2/Cookie", redirectCookies),
path("/categorias/3/Cookie", redirectCookies),
path('/categorias/1/Tienda', redirectTienda),
path("/categorias/2/Tienda", redirectTienda),
path("/categorias/3/Tienda", redirectTienda),

]