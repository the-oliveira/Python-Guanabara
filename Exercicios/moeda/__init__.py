def dobro(valor=0, formato=False):
    """
    Função para retornar o dobro de um valor informado.
    :param valor: Recebe um valor qualquer através de um input ou manualmente.
    :param formato: (opcional) Caso queira que o valor retorne como monetário, adicionar o parametro True.
    :return: Dobro do valor informado.
    """
    res = dobro = valor * 2
    return res if formato == False else moeda(res)


def metade(valor=0, formato=False):
    """
    Função para retornar o valor informado pela metade.
    :param valor: Recebe um valor qualquer através de um input ou manualmente.
    :param formato: (opcional) caso queira que o valor retorne como monetário, adicionar o parametro True.
    :return: Retorna a metade do valor.
    """
    res = metade = valor / 2
    return res if formato == False else moeda(res)


def aumenta(valor=0, aumento=0, formato=False):
    """
    Função para aumentar percentualmente um valor x.
    :param valor: Recebe um valor qualquer através de um input ou manualmente.
    :param aumento: Define o numero porcento que irá aumentar o valor informado.
    :param formato: (opcional) Caso queira formatar para monetário o valor informado adicionar o parametro True.
    :return: Valor com acréscimo baseado no parametro aumento.
    """
    res = dez = (valor * aumento / 100) + valor
    return res if formato == False else moeda(res)


def desconta(valor=0, desconto=0, formato=False):
    """
    Função para definir a porcentagem de desconto de um valor.
    :param valor: Recebe um valor qualquer através de um input ou manualmente.
    :param desconto: número que será descontado percentualmente do valor informado.
    :param formato: (opcional) utilizar o parametro True para formatar o valor recebido em monetário.
    :return: valor com redução baseado no número informado no parametro desconto.
    """
    res = treze = valor - (valor * desconto / 100)
    return res if formato == False else moeda(res)


def moeda(valor=0, moeda='R$', formato=False):
    """
    Função que irá formatar o valor do input em padrão monetário.
    :param valor: recebe o valor digitado pelo usuário ou manualmente.
    :param moeda: sigla da moeda em que o valor será formatado.
    :param formato: (opcional) caso deseje formatar o valor, basta adicionar o parametro True, assim a formatação sera realizada.
    :return: Valor formatado para a moeda padrão (R$) ou personalizada pelo usuário.
    """
    return f'{moeda}{valor:>.2f}'.replace('.', ',')


def resumo(valor=0, aumentando=0, descontando=0):
    """
    Resumo da formatação de um valor monetário, mostrando seu dobro, metade, aumento e desconto
    :param valor: float inserido pelo usuario ou manualmente.
    :param aumentando: numero equivalente ao quanto porcento irá aumentar o parametro valor
    :param descontando: numero equivalente ao quanto porcento ele irá descontar do parametro valor
    :return: Formatação dos valores.
    """
    print('=' * 30)
    print(f'{"Analisando Valores":^30}')
    print('=' * 30)
    print(f'Preço analisado:\t {moeda(valor)}')
    print(f'Dobro do preço: \t {dobro(valor, True)}')
    print(f'Metade do valor:\t {metade(valor, True)}')
    print(f'Aumentando {aumentando}% :\t {aumenta(valor, aumentando, True)}')
    print(f'Descontando {descontando}% :\t {desconta(valor, descontando, True)}')
    print('=' * 30)
