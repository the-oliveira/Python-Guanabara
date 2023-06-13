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


def resumo(valor=0, aumentando=0, descontando=0):
    print('=' * 30)
    print(f'{"Analisando Valores":^30}')
    print('=' * 30)
    print(f'Preço analisado:{moeda(valor):>12}')
    print(f'Dobro do preço:{dobro(valor, True):>12}')
    print(f'Metade do valor:{metade(valor, True):>12}')
    print(f'Aumentando {aumentando}% :{aumenta(valor, aumentando, True):>12}')
    print(f'Descontando {descontando}% :{desconta(valor, descontando, True):>12}')
    print('=' * 30)
