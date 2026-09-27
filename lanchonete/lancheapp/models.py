from django.db import models

# Create your models here.

class ItemCardapio(models.Model):
    nome = models.CharField('Nome', max_length=100, default="")
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Estoque', default=0)
    categoria = models.CharField('Categoria', choices={ # No site, você só vai poder escolher uma dessas opções.
        '1': 'Sanduíches',
        '2': 'Salgados',
        '3': 'Bebidas'
    },max_length=100)

    def __str__(self):
        return f"{self.nome} / {self.preco} / {self.estoque} / {self.categoria}"
