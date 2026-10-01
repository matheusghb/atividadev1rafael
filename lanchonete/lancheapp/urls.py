from django.urls import path
from .views import index, Pedido

urlpatterns = [
    path('', index, name="index"),
    path('pedido/<int:id>', Pedido, name="Pedido")
]