n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
escolha = 0
while escolha != 5:
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] MUDAR OS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    escolha = int(input('Escolha a ação que deseja realizar: '))
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é igual a {soma}')
        print('='*20)
    if escolha == 2:
        mult = n1 * n2
        print(f'Se multiplicarmos {n1} por {n2} temos o resultado de {mult}')
        print('='*20)
    if escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior valor entre {n1} e {n2} é o {maior}')
        print('='*20)
    if escolha == 4:
        n1 = float(input('Digite outro número: '))
        n2 = float(input('Digite outro número: '))
        print('='*20)
    if escolha == 5:
        print('Volte sempre!')
        print('='*20)
        exit()




