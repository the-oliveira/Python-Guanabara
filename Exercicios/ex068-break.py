from random import randint
from time import sleep
perder = 0
vitorias = 0
print('=' * 70)
print('\033[1:32mBEM-VINDO! VAMOS JOGAR PAR OU ÍMPAR!\033[m')
print('=' * 70)
while perder == 0:
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
            print('Você ganhou! Vamos continuar!')
            print('=' * 70)
        else:
            sleep(1)
            perder += 1
            break
    else:
        sleep(1)
        print(f'A soma deu {soma}, portanto o resultado foi ÍMPAR!')
        if jogador == 'IMPAR':
            vitorias += 1
            sleep(1)
            print('=' * 70)
            print('Você ganhou! Vamos continuar!')
            print('=' * 70)
        else:
            perder += 1
            break
sleep(1)
print('='*70)
print(f'Você perdeu! durante seu percurso você ganhou {vitorias} vez(es), tente novamente!')
print('='*70)
