# help() função que puxa um manual de ajuda para varias funcionalidades do python e dos modulos, é uma ajuda interativa
# docstrings = são informações sobre uma função que você criou, é fácil de definir, basta abrir 3 aspas duplas """ """
def contador(i, f, p):
    """

    :param i: Define o ponto de partida da contagem.
    :param f: Define o final da contagem.
    :param p: Define de quantos em quantos números ele irá contar.
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end=' ')
        c += p
    print('fim!')


contador(1,20,1)
help(contador)

