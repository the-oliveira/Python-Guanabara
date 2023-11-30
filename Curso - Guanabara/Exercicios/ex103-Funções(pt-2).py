def ficha(jog='<Desconhecido>', g=0, a=0):
    """
    Programa que retorna os dados de um jogador.
    :param j: String com o nome do jogador
    :param g: Quantidade de gols do jogador
    :param a: Quantidade de assistências do jogador
    :return: String com os dados informados.
    """
    j = str(input('Nome do jogador: '))
    if j.strip() == '':
        j = jog
    gols = str(input('Quantidade de gols: '))
    if gols.isnumeric() == False:
        gols = g
    else:
        g = gols
    assist = str(input('Quantidade de assistências: '))
    if assist.isnumeric() == False:
        assist = a
    else:
        a = assist
    return print(f'O jogador {j} fez {g} gols e {a} assistências no campeonato!')


print('=' * 60)
ficha()
print('=' * 60)
help(ficha)