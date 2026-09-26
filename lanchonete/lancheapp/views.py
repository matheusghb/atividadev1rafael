from django.shortcuts import render
from .models import ItemCardapio as Cardapio

# Create your views here.
def index(request):
    items = Cardapio.objects.all()
    conteudo = {
        'item': items
    }
    return render(request, 'index.html', conteudo)

def Pedido(request, id):
    item = Cardapio.objects.get(id=id)
    conteudo = {
        'pedido': item
    }
    return render(request, 'pedido.html', conteudo)