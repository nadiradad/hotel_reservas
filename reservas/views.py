from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservaForm
from .models import Reserva

# Create your views here.
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            if request.user.is_authenticated:
                reserva.creado_por = request.user
            reserva.save()
            return redirect('reservas:detalle_reserva', pk=reserva.pk)
    else:
        form = ReservaForm()
    return render(request, 'reservas/reserva_form.html', {'form': form})

def detalle_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    return render(request, 'reservas/detalle.html', {'reserva': reserva})
