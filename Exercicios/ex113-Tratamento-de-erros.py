def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
            valor = n
            break
        except (TypeError, ValueError):
            print(f'\033[1:31m Erro, digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print(f'\033[1:31mUsuário interrompeu o programa!\033[m')
            valor = 0
            break
    return valor


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
            valor = n
            break
        except (ValueError, TypeError):
            print(f'\033[1:31mErro, digite um número válido\033[m')
        except KeyboardInterrupt:
            print('\033[1:31mUsuário interrompeu o programa!\033[m')
            valor = 0
            break
    return valor


inteiro = leiaint('Digite um número inteiro: ')
numerofloat = leiafloat('Digite um número real: ')
print(f'Você digitou o número inteiro: {inteiro} e o real foi: {numerofloat}')
