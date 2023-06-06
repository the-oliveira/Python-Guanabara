from time import sleep
cores = ('\033[m',             #limpa    0
         '\033[1;34;40m',      #Azul     1
         '\033[1;36;40m',      #Ciano    2
         '\033[1:30:41m',      #Vermelho 3
         '\033[1:35m'          #Magenta  4
         )


def Pyhelp(comando):
    titulo(f'ACESSANDO O MANUAL \'{comando}\'', 1)
    sleep(2)
    print(cores[4], end='')
    help(comando)
    print(cores[0], end='')


def titulo(msg, cor):
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print('=' * tamanho)
    print(f'  {msg}')
    print('=' * tamanho)
    print(cores[0], end='')
    sleep(1)

while True:

    titulo('SISTEMA DE AJUDA PYHELP', 3)
    comando = str(input('\033[1:32:40m[PyHELP]   DIGITE UM COMANDO OU BIBLIOTECA: '))
    if comando.lower() == 'fim':
        titulo('[PyHELP] Fim do programa! Volte sempre!', 2)
        break
    else:
        Pyhelp(comando)

