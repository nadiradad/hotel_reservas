from django.contrib import admin
from .models import Pago

# Register your models here.
@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):   
    list_display = ('reserva', 'monto', 'metodo', 'estado', 'fecha_pago', 'creado_en')
    list_filter = ('metodo', 'estado', 'fecha_pago')
    search_fields = ('reserva__id', 'referencia')
    ordering = ('fecha_pago',)