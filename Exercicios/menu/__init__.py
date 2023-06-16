def menuprincipal():
    """
    Menu interativo para ver, cadastrar ou sair do sistema, feito com tratamento de erro.
    :return: None
    """
    print('=' * 40)
    print(f'\033[1:34m{"MENU PRINCIPAL":^40}\033[m')
    print('=' * 40)
    print('\033[1:36m1 - Ver pessoas cadastradas\033[m')
    print('\033[1:36m2 - Cadastrar nova Pessoa\033[m')
    print('\033[1:36m3 - Sair do Sistema\033[m')
    print('=' * 40)
    escolha = 0
    while True:
        try:
            escolha = int(input('\033[1:35mSua opção: \033[m'))
            if escolha == 1:
                print('=' * 40)
                print('oi')
                print('=' * 40)
            elif escolha == 2:
                print('=' * 40)
                print('oi 2')
                print('=' * 40)
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


