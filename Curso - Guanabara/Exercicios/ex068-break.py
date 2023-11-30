from random import randint
from time import sleep
vitorias = 0
print('=' * 70)
print('\033[1:35mBEM-VINDO! VAMOS JOGAR PAR OU ÍMPAR!\033[m')
print('=' * 70)
while True:
    jogador = str(input('Escolha PAR ou IMPAR: ')).upper().strip()
    if jogador == 'PAR':
        computador = 'IMPAR'
    elif jogador != 'PAR' and jogador != 'IMPAR':
        jogador = str(input('Escolha inválida, digite novamente: '))
    else:
        computador = 'PAR'
    nplayer = int(input('Digite um número: '))
    ncpu = randint(0, 100)
    soma = nplayer + ncpu
    if soma % 2 == 0:
        sleep(1)
        print(f'A soma deu {soma}, portanto o resultado foi PAR!')
        if jogador == 'PAR':
            vitorias += 1
            sleep(1)
            print('=' * 70)
            print('\033[1:32mVocê ganhou! Vamos continuar!\033[m')
            print('=' * 70)
        else:
            sleep(1)
            break
    else:
        sleep(1)
        print(f'A soma deu {soma}, portanto o resultado foi ÍMPAR!')
        if jogador == 'IMPAR':
            vitorias += 1
            sleep(1)
            print('=' * 70)
            print('\033[1:32mVocê ganhou! Vamos continuar!\033[m')
            print('=' * 70)
        else:
            break
sleep(1)
print('='*70)
print(f'\033[1:31mVocê perdeu! durante seu percurso você ganhou {vitorias} vez(es), tente novamente!\033[m')
print('='*70)
