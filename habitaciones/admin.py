from django.contrib import admin
from .models import TipoHabitacion, Habitacion

# Register your models here.
@admin.register(TipoHabitacion)
class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_noche', 'capacidad')
    search_fields = ('nombre',)
    list_filter = ('capacidad',)
    
@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo', 'activa')
    search_fields = ('numero',)
    list_filter = ('tipo', 'activa')