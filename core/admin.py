from django.contrib import admin
from .models import ItemVenda, Venda, Produto, Cliente, LocalAtendimento

# Register your models here.
admin.site.register(Cliente)
admin.site.register(LocalAtendimento)
admin.site.register(Venda)
admin.site.register(Produto)
admin.site.register(ItemVenda)
