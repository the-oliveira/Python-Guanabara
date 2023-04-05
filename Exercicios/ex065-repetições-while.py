continuar = 's'
total = 0
maior = 0
menor = 0
termos = 0
lista = []
while continuar == 's':
    n1 = int(input('Digite um número: '))
    lista.append(n1)
    total += n1
    termos += 1
    continuar = str(input('Deseja continuar? [S/N] ')).lower().strip()
media = total / termos
print(f'A média entre todos os termos digitado é de {media}')
print(f'O maior número digitado foi {max(lista, key=int)}')
print(f'O menor número digitado foi {min(lista, key=int)}')
