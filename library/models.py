import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    ciudad_nacimidento = models.CharField(max_length=200)
    edad = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Book(models.Model):
    Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    nombre_libro = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre_libro

    def was_published_recently(self):
        return self.fecha_publicacion >= timezone.now() - datetime.timedelta(days=1)