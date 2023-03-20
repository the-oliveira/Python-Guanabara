continuar = 's'
med = 0
maior = 0
menor = 0
termos = 1

while continuar == 's':
    n1 = int(input('Digite um número: '))
    med = med + n1
    termos += 1
    if n1 > maior:
        n1 = maior
    elif n1 < menor:
        n1 = menor
    continuar = str(input('Deseja continuar? [S/N] ')).lower().strip()


media = med/(termos - 1)
print(f'A média entre todos os termos digitado é de {media}')
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
