from random import sample
tupla = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
sorteio = sample(tupla, 5)
print(sorted(sorteio))
print(f'O menor valor foi de {min(sorteio)}')
print(f'O maior valor foi de {max(sorteio)}')
