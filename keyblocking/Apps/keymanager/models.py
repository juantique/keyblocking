from django.db import models
from datetime import datetime

# Create your models here.

class Tblusuario(models.Model):
    # Id_Usuario(PK)
    # Id_Pagina(FK)
    # Id_Tipo_Documento(FK)
    # Id_Genero(FK)
    # Id_Ciudad(FK)
    Nombre_Usuario = models.CharField(max_length=35)
    Apellido_Parterno = models.CharField(max_length=35)
    Apellido_Materno = models.CharField(max_length=35)
    No_Documento = models.CharField(max_length=35)
    Contraseña = models.CharField(max_length=100)
    Correo_Usuario = models.EmailField()
    Fecha_Nacimiento = models.DateTimeField(auto_now_add=True)
    Telefono = models.CharField(max_length=35)
    Direccion_Domicilio = models.CharField(max_length=35)
    Correo_Alterno = models.EmailField()

class Tbltipodocumento(models.Model):
    #Id_Tipo_Documento(PK)
    Id_Tipo_Documento = models.OneToOneField(Tblusuario, null=True, blank=False, on_delete=models.CASCADE)
    Descripcion_Documento = models.CharField(max_length=35)
    
class Tblciudad(models.Model):
    #Id_Ciudad(PK)
    Id_Ciudad = models.OneToOneField(Tblusuario, null=True, blank=False, on_delete=models.CASCADE)
    Descripcion_Ciudad = models.CharField(max_length=35)

class Tblgenero(models.Model):
    #Id_Genero(PK)
    Id_Genero = models.OneToOneField(Tblusuario, null=True, blank=False, on_delete=models.CASCADE)
    Descripcion_Genero = models.TextField(max_length=400)

class Tblpagina(models.Model):
    #Id_Pagina(PK)
    #Id_Usuario(FK)
    Id_Usuario = models.ForeignKey(Tblusuario, null=True, blank=False, on_delete=models.CASCADE)
    Nombre_Pagina = models.CharField(max_length=35)
    Url_Pagina = models.CharField(max_length=35)
    Correo_Pagina = models.EmailField()
    Contraseña_Pagina = models.CharField(max_length=100)
    Descripcion_Pagina = models.CharField(max_length=100)