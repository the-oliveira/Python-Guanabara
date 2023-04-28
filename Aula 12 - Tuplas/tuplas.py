#Variaveis compostas = armazenam mais de um valor na variavel
#As tuplas são imutaveis (não podem ser modificadas durante o funcionamento do programa)
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
for c in lanche:
    print(f'Bora pedir um(a) {c}')
print('Agora sim')

#se precisar da posição, usar:

# for posição, c in enumerate(lanche):
#   print(f'Para mostrar o elemento da tupla {c} e a posição {posição}'

#Ou utilizar o len em uma estrutura for:
# for cont in range (0, len(lanche)):
#   print(f'valor da tupla {lanche[cont]} na posição {cont}'
