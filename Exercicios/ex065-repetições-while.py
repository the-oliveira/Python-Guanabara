continuar = 's'
med = 0
maior = 0
menor = 0
termos = 1
lista = []
while continuar == 's':
    n1 = int(input('Digite um número: '))
    lista.append(n1)
    med = med + n1
    termos += 1
    continuar = str(input('Deseja continuar? [S/N] ')).lower().strip()


media = med/(termos - 1)
print(f'A média entre todos os termos digitado é de {media}')
print(f'O maior número digitado foi {max(lista, key=int)}')
print(f'O menor número digitado foi {min(lista, key=int)}')
