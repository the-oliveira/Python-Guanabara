from time import sleep
from utilidades.menu.menucreate import *

arq = 'projetinhofinal.txt'
if arquivoExiste(arq):
    print('Abrindo arquivo... por favor aguarde!')
    sleep(1)
else:
    print('Arquivo não encontrado.')
    sleep(0.5)
    print('Criando novo arquivo... por favor aguarde!!')
    sleep(1)
    criarArquivo(arq)
menuprincipal(arq)
escolha = 0
while True:
    try:
        escolha = int(input('\033[1:35mSua opção: \033[m'))
        if escolha == 1:
            lerAqruivo(arq)
            print('=' * 40)
        elif escolha == 2:
            print('=' * 40)
            print('oi 2')
            print('=' * 40)
        elif escolha == 3:
            print('=' * 40)
            print(f'\033[1:32m{"Programa encerrado, volte sempre!!":^40}\033[m')
            print('=' * 40)
            break
        else:
            print('=' * 40)
            print('\033[1:31mOpção inválida!\033[m'.center(50))
            print('=' * 40)
    except (ValueError, TypeError):
        print('=' * 40)
        print(f'\033[1:31mEntrada inválida!\033[m'.center(50))
        print('=' * 40)
        continue
    except KeyboardInterrupt:
        print()
        print('=' * 40)
        print(f'\033[1:31mPrograma interrompido pelo usuário.\033[m'.center(50))
        print('=' * 40)
        break
