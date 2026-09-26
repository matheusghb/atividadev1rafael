from django.contrib import admin
from .models import ItemCardapio

class ItemAdmin(admin.ModelAdmin):
    list_display = "nome","preco","estoque","categoria"

# Register your models here.

admin.site.register(ItemCardapio, ItemAdmin)