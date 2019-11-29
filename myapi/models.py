from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    edad = models.CharField(max_length=60)
    sexo = models.CharField(max_length=60)
    direccion = models.TextField(max_length=1000)
    carrera = models.CharField(max_length=60)    
    delete = models.BooleanField(default = False)


class Carrera(models.Model):        
    nombre_carrera = models.CharField(max_length=60)
    delete = models.BooleanField(default = False)
    re_alumno= models.ForeignKey(Alumno, related_name='carreras', on_delete=models.CASCADE)#null=false
