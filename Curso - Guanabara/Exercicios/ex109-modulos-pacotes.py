from utilidades import moeda
#Exercicio simplificando a chamada da conversão de moeda, para isso utilizamos um if antes de dar return no 'res'
#Adicionamos também a condicional True para formato
p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O Dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Descontando 10% de {moeda.moeda(p)} o valor fica {moeda.aumenta(p, 10, True)}')
print(f'Descontando 13% de {moeda.moeda(p)} o valor fica {moeda.desconta(p, 13, True)}')