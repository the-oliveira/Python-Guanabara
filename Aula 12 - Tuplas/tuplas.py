#Variaveis compostas = armazenam mais de um valor na variavel
#As tuplas são imutaveis (não podem ser modificadas durante o funcionamento do programa)
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
for c in lanche:
    print(f'Bora pedir um(a) {c}')
    #é possivel usar o print(sorted) para printar a tupla em ordem.
print('Agora sim')


#se precisar da posição, usar:
# for posição, c in enumerate(lanche):
#   print(f'Para mostrar o elemento da tupla {c} e a posição {posição}'

#Ou utilizar o len em uma estrutura for:
# for cont in range (0, len(lanche)):
#   print(f'valor da tupla {lanche[cont]} na posição {cont}'

#É possível agregar o valor de duas tuplas, criando separadamente e depois criando uma terceira com o valor de a + b ou b + a.
#Podemos usar o print(variavel.count(valor)) caso precisamos ver quantas vezes certo valor é encontrado dentro da tupla.
#Também existe o print(variavel.index(valor)), que nos mostra a posição em que o valor se encontra na tupla.

#É possível deletar uma variavel utilizando o:  del(variavel)