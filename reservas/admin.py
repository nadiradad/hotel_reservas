from django.contrib import admin
from .models import Reserva
from pagos.models import Pago

# Register your models here.
class PagoInline(admin.TabularInline):
    model = Pago
    extra = 1
    readonly_fields = ('creado_en',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id','cliente','habitacion','fecha_entrada','fecha_salida','estado','creado_en')
    list_filter = ('estado','fecha_entrada')
    search_fields = ('cliente__nombre','cliente__apellido','habitacion__numero')
    inlines = [PagoInline]
