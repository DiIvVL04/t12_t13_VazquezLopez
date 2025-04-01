from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    matricula = models.CharField(max_length=11, unique=True)
    correo = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.nombre