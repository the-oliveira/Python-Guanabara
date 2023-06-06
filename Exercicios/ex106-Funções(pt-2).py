from time import sleep
cores = ('\033[m',             #limpa    0
         '\033[1;34;40m',      #Azul     1
         '\033[1;36;40m',      #Ciano    2
         '\033[1:30:41m'       #Vermelho 3
         )
def Pyhelp(comando):
    help(comando)

def titulo(msg, cor):
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print('=' * tamanho)
    print(f'  {msg}')
    print('=' * tamanho)
    print(cores[0], end='')

while True:

    titulo('SISTEMA DE AJUDA PYHELP', 3)
    comando = str(input('\033[1:32:40m[PyHELP]   DIGITE UM COMANDO OU BIBLIOTECA: '))
    if comando.lower() == 'fim':
        titulo('[PyHELP] Fim do programa! Volte sempre!', 2)
        sleep(1)
        break
    else:
        Pyhelp(comando)
    sleep(0.5)

