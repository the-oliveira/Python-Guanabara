#listas são entre []
#listas podem ser alteradas
#variavel.append('valor') para adicionar algum valor no final da lista
#variavel.insert(posição,'valor') para inserir um valor em uma posição especifica na lista


#deletar valores na liista:
#del variavel[posição]
#variavel.pop(posição) = normalmente usado para deletar o ultimo valor mas pode escolher a posição entre parenteses
#variavel.remove('valor') = para deletar um valor especifico da lista

#Também da para criar listas utilizando a declaração:
#variavel = list(range(posição inicial, posição final)), ele irá criar uma lista com os valores dentro da range

#variavel.sort() ordena a lista
#variavel.sort(reverse=True) para ordenar do maior pro menor

#len(variavel) para saber o tamanho da lista
num = [0,1,2,3,4,5,6,7,8,9]
print(num)
num[0] = 8
print(num)
num.append(22)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
num.insert(1, 2000)
num.pop()
del num[0]
num.remove(2000)
print(num)
print(f'Número de elementos na lista: {len(num)}')

