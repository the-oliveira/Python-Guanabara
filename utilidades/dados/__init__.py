def leiadinheiro (msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[1:31mERRO: {entrada} é um preço inválido, digite novamente!\033[m')
        else:
            valido = True
            return float(entrada)


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