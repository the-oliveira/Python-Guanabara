def ficha(j='<Desconhecido>', g=0, a=0):
    j = str(input('Nome do jogador: '))
    g = int(input('Quantidade de gols: '))
    a = int(input('Quantidade de assistências: '))
    return print(f'O jogador {j} fez {g} gols e {a} assistências no campeonato!')


print('=' * 40)
ficha()
print('=' * 40)
