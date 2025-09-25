from django.contrib import admin
from .models import Cliente

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'dni', 'creado_en')
    search_fields = ('nombre', 'apellido', 'email', 'dni')
    list_filter = ('creado_en',)
    ordering = ('apellido', 'nombre')