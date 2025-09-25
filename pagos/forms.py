from django import forms
from .models import Pago

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['monto','metodo','referencia','fecha_pago','estado']
