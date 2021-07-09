from django.db import models

# Create your models here.

class Desarrollador(models.Model):
    nombre_desarrollador = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_desarrollador

class Juego(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()
    categoria = models.CharField(max_length=50)
    desarrollador = models.ForeignKey(Desarrollador, on_delete=models.PROTECT)
    fecha_lanzamiento = models.DateField()

    def __str__(self):
        return self.nombre