from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = 0
while escolha != 5:
    print('=-='*20)
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] MUDAR OS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    print('=-='*20)
    escolha = int(input('Escolha a ação que deseja realizar: '))
    if escolha == 1:
        soma = n1 + n2
        print(f'\033[1:34mA soma de {n1} + {n2} é igual a {soma}\033[m')
        sleep(2)
    elif escolha == 2:
        mult = n1 * n2
        print(f'\033[1:34mSe multiplicarmos {n1} por {n2} temos o resultado de {mult}\033[m')
        sleep(2)
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'\033[1:34mO maior valor entre {n1} e {n2} é o {maior}\033[m')
        sleep(2)
    elif escolha == 4:
        n1 = int(input('Digite outro número: '))
        n2 = int(input('Digite outro número: '))
        sleep(2)
    elif escolha == 5:
        print('\033[1:34mVolte sempre!\033[m')
        sleep(2)
        exit()
    else:
        print('\033[1:31mComando inválido, tente novamente!\033[m')




