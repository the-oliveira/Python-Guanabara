def menuprincipal():
    print('=' * 30)
    print(f'{"MENU PRINCIPAL":^30}')
    print('=' * 30)
    escolha = 0
    while True:
        try:
            escolha = int(input('Escolha uma opção: '))
            if escolha == 1:
                print('oi')
            elif escolha == 2:
                print('oi 2')
            else:
                print('=' * 40)
                print(f'\033[1:32m{"Programa encerrado, volte sempre!!":^40}\033[m')
                print('=' * 40)
                break
        except (ValueError, TypeError):
            print(f'\033[1:31mEntrada de valor inválida, tente novamente.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[1:31mPrograma interrompido pelo usuário.\033[m')
            break


