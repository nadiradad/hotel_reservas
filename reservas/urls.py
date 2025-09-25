from django.urls import path
from . import views

app_name = 'reservas'

urlpatterns = [
    path('nueva/', views.crear_reserva, name='crear_reserva'),
    path('<int:pk>/', views.detalle_reserva, name='detalle_reserva'),
]
