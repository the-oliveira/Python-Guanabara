def leiaint(n):
    int(input(n))
    while n not in range(-99999, 999999999):
        print('Comando inválido! tente novamente.')
        n = leiaint('Digite um número: ')



n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}!')