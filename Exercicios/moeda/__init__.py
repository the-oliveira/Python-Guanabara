def dobro(valor=0, formato=False):
    res = dobro = valor * 2
    return res if formato == False else moeda(res)


def metade(valor=0, formato=False):
    res = metade = valor / 2
    return res if formato == False else moeda(res)


def aumenta(valor=0, aumento=0, formato=False):
    res = dez = (valor * aumento / 100) + valor
    return res if formato == False else moeda(res)


def desconta(valor=0, desconto=0, formato=False):
    res = treze = valor - (valor * desconto / 100)
    return res if formato == False else moeda(res)


def moeda(valor=0, moeda='R$', formato=False):
    return f'{moeda}{valor:>.2f}'.replace('.', ',')
