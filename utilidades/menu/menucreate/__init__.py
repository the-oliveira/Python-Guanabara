from utilidades.menu.arquivo import *
def menuprincipal(nome):
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
