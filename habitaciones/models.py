from django.db import models

# Create your models here.
class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    precio_noche = models.DecimalField(max_digits=8, decimal_places=2)
    capacidad = models.PositiveSmallIntegerField(default=2)

    def __str__(self):
        return f"{self.nombre} - {self.precio_noche} / noche"

class Habitacion(models.Model):
    numero = models.CharField(max_length=10, unique=True)  # ej. "101"
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.PROTECT)
    activa = models.BooleanField(default=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"Hab {self.numero} - {self.tipo.nombre}"