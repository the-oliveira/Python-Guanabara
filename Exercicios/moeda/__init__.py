def dobro(valor):
    dobro = valor * 2
    return dobro


def metade(valor):
    metade = valor / 2
    return metade


def aumenta(valor, aumento=0):
    dez = (valor * aumento / 100) + valor
    return dez


def desconta(valor, desconto=0):
    treze = valor - (valor * desconto / 100)
    return treze

