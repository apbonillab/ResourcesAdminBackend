from datetime import datetime

from django.db.models import ForeignKey

# Create your views here.
from django.db import models

class Tipo_Recurso(models.Model):
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre

class Responsable(models.Model):
    nombres = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    usuario = models.CharField(max_length=50, null=False)
    rol = ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return '%d: %s' % (self.id, self.nombres)

class Recurso(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=100, null=False)
    tipoRecurso = ForeignKey(Tipo_Recurso,related_name='tipoRecurso', on_delete=models.CASCADE)
    idSolicitud = models.CharField(max_length=50, null=False)
    idProyecto = models.CharField(max_length=50, null=False)
    descripcionSolicitud = models.CharField(max_length=300, null=False)
    estado = ForeignKey(Estado,related_name='estado', on_delete=models.CASCADE, default="Creado")
    auditor = ForeignKey(Responsable,related_name='auditor', on_delete=models.CASCADE,null=True)
    def __str__(self):
        return '%d: %s' % (self.id, self.nombre)

class Control_Comentarios(models.Model):
    idRecurso = ForeignKey(Recurso, related_name='recurso', on_delete=models.CASCADE)
    comentario = models.CharField(max_length=1000, null=False)
    revisor = ForeignKey(Responsable, related_name='responsable', on_delete=models.CASCADE)
    descripcion =  models.CharField(max_length=1000, null=True)
    fecha = models.DateField(default=datetime.now, blank=True)
    estado = models.CharField(max_length=20, null=False)

class Recurso_Responsable(models.Model):
    responsable = ForeignKey(Responsable)
    rescursos = ForeignKey(Recurso)

class Recurso_Intermedio(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    tipoRecurso = ForeignKey(Tipo_Recurso)
    estado = ForeignKey(Estado)
    descripcion = models.CharField(max_length=200, null=False)
    recursoPrincipal = ForeignKey(Recurso)
    responsable = ForeignKey(Responsable)

    def __str__(self):
        return self.nombre

class Lista_Chequeo(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=200, null=False)
    asignado = ForeignKey(Responsable)

    def __str__(self):
        return self.nombre


class Resultado_ListaChequeo(models.Model):
    recurso = ForeignKey(Recurso_Intermedio)
    itemChequeo = ForeignKey(Lista_Chequeo)
    resultado = models.BooleanField()