from django import forms
from .models import Reserva
from django.core.exceptions import ValidationError

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente','habitacion','fecha_entrada','fecha_salida','estado']

    def clean(self):
        cleaned = super().clean()
        # pasar datos al instance y volver a validar con clean() del modelo
        self.instance.cliente = cleaned.get('cliente')
        self.instance.habitacion = cleaned.get('habitacion')
        self.instance.fecha_entrada = cleaned.get('fecha_entrada')
        self.instance.fecha_salida = cleaned.get('fecha_salida')
        try:
            self.instance.clean()
        except ValidationError as e:
            raise forms.ValidationError(e.messages)
        return cleaned
