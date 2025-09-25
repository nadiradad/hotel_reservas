from django.db import models
from django.utils import timezone
from decimal import Decimal

# Create your models here.
class Pago(models.Model):
    METODO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
        ('otro', 'Otro'),
    ]
    ESTADO_CHOICES = [
        ('completado', 'Completado'),
        ('pendiente', 'Pendiente'),
        ('reembolsado', 'Reembolsado'),
    ]

    reserva = models.ForeignKey('reservas.Reserva', on_delete=models.CASCADE, related_name='pagos')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=20, choices=METODO_CHOICES)
    referencia = models.CharField(max_length=255, blank=True, null=True)  # id transacción, cupón, etc.
    fecha_pago = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='completado')
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_metodo_display()} {self.monto} — Reserva {self.reserva_id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # actualizar estado de la reserva si queda sin saldo
        reserva = self.reserva
        if reserva.total_pagado() >= reserva.total_precio():
            if reserva.estado != 'confirmada':
                reserva.estado = 'confirmada'
                reserva.save(update_fields=['estado'])
