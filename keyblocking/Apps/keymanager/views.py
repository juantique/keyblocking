from django.shortcuts import render
from rest_framework import serializers, viewsets

# importamos los serializadores que creamos desde el archivo serializers
from .serializers import UsuarioSerializer
from .serializers import TipodocumentoSerializer
from .serializers import CiudadSerializer
from .serializers import GeneroSerializer
from .serializers import PaginaSerializer

# importamos los modelos
from .models import Tblusuario
from .models import Tbltipodocumento
from .models import Tblciudad
from .models import Tblgenero
from .models import Tblpagina

# ViewSets define the view behavior.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Tblusuario.objects.all()
    serializer_class = UsuarioSerializer

class TipodocumentoViewSet(viewsets.ModelViewSet):
    queryset = Tblusuario.objects.all()
    serializer_class = TipodocumentoSerializer

class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Tblusuario.objects.all()
    serializer_class = CiudadSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Tblusuario.objects.all()
    serializer_class = GeneroSerializer

class PaginaViewSet(viewsets.ModelViewSet):
    queryset = Tblusuario.objects.all()
    serializer_class = PaginaSerializer
# Create your views here.
