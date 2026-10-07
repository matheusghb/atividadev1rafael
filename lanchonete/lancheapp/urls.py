from django.urls import path
from .views import index, Pedido, Bebidas, Salgados, Sanduiches, sobrenos

urlpatterns = [
    path('', index, name="index"),
    path('pedido/<int:id>', Pedido, name="Pedido"),
    path('Bebidas', Bebidas, name="Bebidas"),
    path('Salgados', Salgados, name="Salgados"),
    path('Sanduiches', Sanduiches, name="Sanduiches"),
    path('sobrenos', sobrenos, name='sobrenos')
]