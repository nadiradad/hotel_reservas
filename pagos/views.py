from django.shortcuts import render, redirect, get_object_or_404
from .forms import PagoForm
from reservas.models import Reserva

# Create your views here.
def registrar_pago(request, reserva_pk):
    reserva = get_object_or_404(Reserva, pk=reserva_pk)
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = form.save(commit=False)
            pago.reserva = reserva
            pago.save()
            return redirect('reservas:detalle_reserva', pk=reserva.pk)
    else:
        form = PagoForm()
    return render(request, 'pagos/pago_form.html', {'form': form, 'reserva': reserva})
