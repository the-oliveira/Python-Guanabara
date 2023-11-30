from utilidades import moeda
#Exercicio adicionando a formatação da moeda padrão, substituindo os '.' pelas ',' e acrescentando R$ direto da função.
p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O Dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Descontando 10% de {moeda.moeda(p)} o valor fica {moeda.moeda(moeda.aumenta(p, 10))}')
print(f'Descontando 13% de {moeda.moeda(p)} o valor fica {moeda.moeda(moeda.desconta(p, 13))}')