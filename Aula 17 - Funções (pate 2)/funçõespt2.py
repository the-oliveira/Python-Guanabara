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

#Parametrôs opcionais são definidos com um valor padrão na hora de declarar a função, por exemplo declarando uma def de soma = 0


def soma (a=0, b=0, c=0):
    """
    Função de soma
    :param a: Recebe o primeiro valor
    :param b: Recebe o segundo valor
    :param c: Recebe o terceiro valor
    :return: none
    """
    s = a+b+c
    print(f'A soma final deu {s}')

soma(1, 2, 3)
soma(1)
soma(10, 2)
soma()

#Variaveis declaradas no programa principal são globais (escopo global), variaveis declaradas em funções são apenas locais (escopo local)
# ou seja, só vão funcionar dentro do escopo da função.