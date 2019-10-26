"""keyblocking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

# importamos el rest framework.
from rest_framework import routers, serializers, viewsets
# importamos los modelos.
from keyblocking.Apps.keymanager.models import Tblusuario
from keyblocking.Apps.keymanager.models import Tbltipodocumento
from keyblocking.Apps.keymanager.models import Tblciudad
from keyblocking.Apps.keymanager.models import Tblgenero
from keyblocking.Apps.keymanager.models import Tblpagina

# importamos las vistas creadas.
from keyblocking.Apps.keymanager.views import UsuarioViewSet
from keyblocking.Apps.keymanager.views import TipodocumentoViewSet
from keyblocking.Apps.keymanager.views import CiudadViewSet
from keyblocking.Apps.keymanager.views import GeneroViewSet
from keyblocking.Apps.keymanager.views import PaginaViewSet

# Los enrutadores proporcionan una manera fácil de determinar automáticamente la configuración de URL.
router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
router.register(r'documento', TipodocumentoViewSet)
router.register(r'ciudad', CiudadViewSet)
router.register(r'genero', GeneroViewSet)
router.register(r'pagina', PaginaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
