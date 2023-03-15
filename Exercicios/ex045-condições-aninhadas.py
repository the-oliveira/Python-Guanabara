from random import randint
jogador = str(input('Pedra, papel ou tesoura? '))
jogador.lower()
computador = randint(1, 3)

if computador == 1:
    jokenpo = str('pedra')
elif computador == 2:
    jokenpo = str('papel')
elif computador == 3:
    jokenpo = str('tesoura')

if computador == 'pedra' and jogador == 'pedra' or computador == 'papel' and jogador == 'papel' or computador == 'tesoura' and computador == 'tesoura':
    print('Empatou!')


