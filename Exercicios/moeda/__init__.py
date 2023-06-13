def dobro(valor=0):
    res = dobro = valor * 2
    return res


def metade(valor=0):
    res = metade = valor / 2
    return res


def aumenta(valor=0, aumento=0):
    res = dez = (valor * aumento / 100) + valor
    return res


def desconta(valor=0, desconto=0):
    res = treze = valor - (valor * desconto / 100)
    return res


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>.2f}'.replace('.', ',')
