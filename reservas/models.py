from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import Sum
from decimal import Decimal

# Create your models here.
class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('finalizada', 'Finalizada'),
    ]

    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    habitacion = models.ForeignKey('habitaciones.Habitacion', on_delete=models.PROTECT)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    creado_por = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_entrada']

    def clean(self):
        # 1) fechas válidas
        if self.fecha_salida <= self.fecha_entrada:
            raise ValidationError("La fecha de salida debe ser posterior a la fecha de entrada.")
        # 2) comprobar solapamiento con reservas activas (no considerar canceladas)
        solapadas = Reserva.objects.filter(
            habitacion=self.habitacion
        ).exclude(pk=self.pk).exclude(
            estado='cancelada'
        ).filter(
            fecha_entrada__lt=self.fecha_salida,
            fecha_salida__gt=self.fecha_entrada
        )
        if solapadas.exists():
            raise ValidationError("La habitación no está disponible en las fechas seleccionadas.")

    def total_noches(self):
        return (self.fecha_salida - self.fecha_entrada).days

    def total_precio(self):
        precio_noche = self.habitacion.tipo.precio_noche
        return precio_noche * self.total_noches()

    def total_pagado(self):
        agg = self.pagos.aggregate(total=Sum('monto'))
        return agg['total'] or Decimal('0.00')

    def saldo(self):
        return self.total_precio() - self.total_pagado()

    def __str__(self):
        return f"Reserva #{self.pk} - {self.cliente} ({self.fecha_entrada} → {self.fecha_salida})"
