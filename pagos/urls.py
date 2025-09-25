from django.urls import path
from . import views

app_name = 'pagos'
urlpatterns = [
    path('registrar/<int:reserva_pk>/', views.registrar_pago, name='registrar_pago'),
]
