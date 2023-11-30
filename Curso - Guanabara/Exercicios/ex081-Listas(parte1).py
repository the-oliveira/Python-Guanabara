lista = []
while True:
    print('=' * 50)
    lista.append(int(input('Digite um valor: ')))
    print('=' * 50)
    continuar = str(input('Deseja digitar um novo valor? [S/N] ')).upper().split()[0]
    while continuar not in'SN':
        continuar = str(input('Deseja digitar um novo valor? [S/N] ')).upper().split()[0]
    if continuar == 'N':
        break
lista.sort(reverse=True)
print('='*40)
print(f'A lista ficou da seguinte forma: {lista}')
print('='*40)
print(f'Foram digitados {len(lista)} valores na lista!')
print('='*40)
if 5 in lista:
    print(f'O valor 5 foi encontrado na lista {lista.count(5)} vezes!')
else:
    print('Não encontrei o número 5 na lista! Uffa..')
print('='*40)