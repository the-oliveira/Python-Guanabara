def ficha(j='<Desconhecido>', g=0, a=0):
    """
    Programa que retorna os dados de um jogador.
    :param j: String com o nome do jogador
    :param g: Quantidade de gols do jogador
    :param a: Quantidade de assistências do jogador
    :return: String com os dados informados.
    """
    j = str(input('Nome do jogador: '))
    g = int(input('Quantidade de gols: '))
    a = int(input('Quantidade de assistências: '))
    return print(f'O jogador {j} fez {g} gols e {a} assistências no campeonato!')


print('=' * 40)
ficha()
print('=' * 40)
