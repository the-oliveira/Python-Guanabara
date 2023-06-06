def ficha(j='<Desconhecido>', g=0, a=0):
    """
    Programa que retorna os dados de um jogador.
    :param j: String com o nome do jogador
    :param g: Quantidade de gols do jogador
    :param a: Quantidade de assistências do jogador
    :return: String com os dados informados.
    """
    j = str(input('Nome do jogador: '))
    if j.strip() == '':
        j = '<Desconhecido>'
    g = str(input('Quantidade de gols: '))
    if g.isnumeric() == False:
        g = 0
    a = str(input('Quantidade de assistências: '))
    if a.isnumeric() == False:
        a = 0
    return print(f'O jogador {j} fez {g} gols e {a} assistências no campeonato!')


print('=' * 60)
ficha()
print('=' * 60)
