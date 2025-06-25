from django.urls import path 
from . import views  

urlpatterns = [
    path("", views.home, name="home"), 
    path("produtos/", views.lista_produtos, name="produtos"),  
    path("clientes/", views.lista_clientes, name="clientes"), 
    path("agenda/", views.lista_agenda, name="agenda"),  
    path( "faturamento/", views.faturamento_mensal, name="faturamento_mensal"),  
    path("mais-vendidos/", views.produtos_mais_vendidos, name="produtos_mais_vendidos"),  
    path("grafico-produtos/", views.grafico_produtos_mais_vendidos, name="grafico_produto"),  
    path("portfolio_produtos/", views.portfolio_produtos, name="portifolio_produtos"),  
]
