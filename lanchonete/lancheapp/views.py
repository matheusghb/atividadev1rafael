from django.shortcuts import render
from .models import ItemCardapio as Cardapio

# Create your views here.
def index(request):
    items = Cardapio.objects.all()
    conteudo = {
        'item': items # Da acesso ao banco de dados ItemCardapio dentro do HTML. 
    }
    return render(request, 'index.html', conteudo)

def Pedido(request, id): # Essa função será utilizada em index.html para receber um id dinamico e formar uma página adaptada ao item escolhido.
    item = Cardapio.objects.get(id=id)
    conteudo = {
        'pedido': item 
    }
    return render(request, 'pedido.html', conteudo)

def Bebidas(request): 
    item = Cardapio.objects.all()
    conteudo = {
        'cat': item 
    }
    return render(request, 'Bebidas.html', conteudo)

def Salgados(request): 
    item = Cardapio.objects.all()
    conteudo = {
        'cat': item 
    }
    return render(request, 'Salgados.html', conteudo)

def Sanduiches(request): 
    item = Cardapio.objects.all()
    conteudo = {
        'cat': item 
    }
    return render(request, 'Sanduiches.html', conteudo)

def sobrenos(request):
    return render(request, 'sobrenos.html')