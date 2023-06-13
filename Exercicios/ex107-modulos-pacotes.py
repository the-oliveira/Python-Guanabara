import moeda
#Exercicio para criar funções iniciais retornando o dobro, metade, acréscimo e decréscimo de valores.
p = float(input('Digite um preço: R$'))
print(f'A metade de R${p:.2f} é R${moeda.metade(p):.2f}')
print(f'O Dobro de R${p:.2f} é R${moeda.dobro(p):.2f}')
print(f'Descontando 10% de R${p:.2f} o valor fica R${moeda.aumenta(p, 10):.2f}')
print(f'Descontando 13% de R${p:.2f} o valor fica R${moeda.desconta(p, 13):.2f}')