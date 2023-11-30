n = int(input('Digite o número de termos que deseja ver da sequência de Fibonacci: '))
inicio = 3
termo1 = 0
termo2 = 1
print(f'{termo1} - {termo2}', end='')
while inicio <= n:
    termo3 = termo1 + termo2
    print(f' - {termo3}', end='')
    termo1 = termo2
    termo2 = termo3
    inicio += 1
print('- FINAL')


