from django.db import models
from datetime import datetime

# Create your models here.
class login (models.Model):
    id_usuario = models.BigIntegerField()
    correo_activo = models.EmailField()
    contraseña = models.CharField(max_length=100)

class usuario(models.Model):
    login = models.BigIntegerField()
    Apellido_Parterno = models.CharField(max_length=35)
    Apellido_Materno = models.CharField(max_length=35)
    Nombre=models.CharField(max_length=35)
    correo_activo = models.EmailField()
    FechaNacimiento = models.DateTimeField(auto_now_add=True)
    SEXO = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXO, default='M')
    Ciudad = models.CharField(max_length=35)

class registro(models.Model):
    id_usuario = models.BigIntegerField()
    Apellido_Parterno = models.CharField(max_length=35)
    Apellido_Materno = models.CharField(max_length=35)
    Nombre=models.CharField(max_length=35)
    Telefono = models.IntegerField()
    Direccion_Domicilio = models.CharField(max_length=35)
    correo_activo = models.EmailField()
    correo_alternativo = models.EmailField()
    contraseña = models.CharField(max_length=100)
    FechaNacimiento = models.DateTimeField(auto_now_add=True)
    SEXO = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXO, default='M')
    Ciudad = models.CharField(max_length=35)

class listado(models.Model):
    id_usuario = models.BigIntegerField()
    Apellido_Parterno = models.CharField(max_length=35)
    Apellido_Materno = models.CharField(max_length=35)
    Nombre=models.CharField(max_length=35)
    id_pagina = models.BigIntegerField()

class formulario_pagina(models.Model):
    id_pagina = models.BigIntegerField()
    #PAGINARED = (('F','Facebook'), ('I','Instagram'), ('T','Twitter'), ('L','Linkedln'), ('YT','YouTube'), ('S','Snapchat'), ('P','Pinterest'), ('NA''Ninguna'))
    PAGINARED = (('F','Facebook'), ('I','Instagram'))
    Pagina_Red = models.CharField(max_length=1, choices=PAGINARED, default = 'N/A')
    #PAGINACOMP = (('A','Amazon'), ('E','Ebay'), ('W','Walmart'), ('A','Alibaba'), ('ML','MercadoLibre'), ('AE','AliExpress'), ('BB','Best Bay'), ('NA''Ninguna'))
    PAGINACOMP = (('A','Amazon'), ('E','Ebay'))
    Pagina_Compra = models.CharField(max_length=35, choices=PAGINACOMP, default = 'N/A')
    Correo_Cuenta = models.EmailField()
    contraseña = models.CharField(max_length=100)
    Descripcion_Cuenta = models.TextField(max_length=400)

class Recuperacion(models.Model):
    correo_activo = models.EmailField()
    correo_alternativo = models.EmailField()
    id_usuario = models.BigIntegerField()
    Telefono = models.IntegerField()