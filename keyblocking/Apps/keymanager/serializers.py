from rest_framework import serializers, viewsets

from keyblocking.Apps.keymanager.models import Tblusuario
from keyblocking.Apps.keymanager.models import Tbltipodocumento
from keyblocking.Apps.keymanager.models import Tblciudad
from keyblocking.Apps.keymanager.models import Tblgenero
from keyblocking.Apps.keymanager.models import Tblpagina

# Serializers define the API representation.
class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tblusuario
        fields = ['Nombre_Usuario', 'Apellido_Parterno', 'Apellido_Materno', 'No_Documento', 'Correo_Usuario', 'Telefono', 'Direccion_Domicilio', 'Correo_Alterno','Fecha_Nacimiento',]

class TipodocumentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tbltipodocumento
        fields = ['Id_Tipo_Documento', 'Descripcion_Documento',]

class CiudadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tblciudad
        fields = ['Id_Ciudad', 'Descripcion_Ciudad',]

class GeneroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tblgenero
        fields = ['Id_Genero', 'Descripcion_Genero',]

class PaginaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tblpagina
        fields = ['Id_Usuario', 'Nombre_Pagina', 'Url_Pagina', 'Correo_Pagina', 'Contraseña_Pagina', 'Descripcion_Pagina',]