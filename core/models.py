from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)
    data_cadastro = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return self.nome
    
class LocalAtendimento(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    data_evento = models.DateField(blank=True, null=True)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    def __str__(self):
        return f"{self.nome} - {self.data_evento}" 
    
class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    local = models.ForeignKey(LocalAtendimento, on_delete=models.CASCADE, null=True, blank=True)
    data_venda = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.cliente.nome} - {self.data_venda}"
    
    @property
    def total_venda(self):
        return sum(item.subtotal for item in self.itens_venda.all())
    
class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens_venda') 
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE) 
    quantidade = models.PositiveIntegerField(default=1) 
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.produto.nome} x {self.quantidade}" 
    
    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario