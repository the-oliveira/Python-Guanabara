def leiaint(msg):
    valido = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = n
            valido = True
            break
        else:
            print(f'\033[1:31mErro, digite um número inteiro válido: \033[m')
    return valor


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}!')