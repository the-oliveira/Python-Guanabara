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

