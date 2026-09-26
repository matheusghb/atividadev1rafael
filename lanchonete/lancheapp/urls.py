from django.urls import path
from .views import index, Pedido

urlpatterns = [
    path('', index, name="Página inicial"),
    path('pedido/<int:id>', Pedido, name="Pedido")
]