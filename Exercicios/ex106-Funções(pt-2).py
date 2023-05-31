def Pyhelp():
    print('\033[1:30:41m=\033[m' * 30)
    print(f'\033[1:30:41m    SISTEMA DE AJUDA PYHELP   \033[m')
    print('\033[1:30:41m=\033[m' * 30)
    comando = input('\033[1:47m[PyHELP]   DIGITE UM COMANDO: \033[1:43m')
    while comando not in 'fim':
        return help(comando)
        comando = input('\033[1:47m[PyHELP]   DIGITE UM COMANDO: \033[1:43m')

Pyhelp()