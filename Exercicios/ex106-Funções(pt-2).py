def Pyhelp():
    from time import sleep
    while True:
        print('\033[1:30:45m=' * 30)
        print(f'\033[1:30:45m    SISTEMA DE AJUDA PYHELP   ')
        print('\033[1:30:45m=' * 30)
        comando = str(input('\033[1:32:40m[PyHELP]   DIGITE UM COMANDO OU BIBLIOTECA: '))
        if comando.lower() == 'fim':
            print('\033[1:30:42m[PyHELP] Fim do programa! Volte sempre!')
            sleep(1)
            break
        sleep(0.5)
        help(comando)


Pyhelp()
