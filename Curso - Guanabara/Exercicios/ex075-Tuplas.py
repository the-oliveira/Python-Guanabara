numero = (int(input('Difite um número: ')),
          int(input('Difite um número: ')),
          int(input('Difite um número: ')),
          int(input('Difite um número: ')))
print(f'O número 9 foi encontrado: {numero.count(9)} vezes na tupla.')
if 3 in numero:
    print(f'A posição do primeiro valor 3 digitado foi: {numero.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
for n in numero:
    if n % 2 == 0:
        print(f'O valor {n} é par')