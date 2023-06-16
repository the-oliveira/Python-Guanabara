from ex115.arquivo import *
from ex115.menu import *
from time import sleep

arq = 'projetinhofinal.txt'
if arquivoExiste(arq):
    print('Abrindo arquivo... por favor aguarde!')
    sleep(1)
else:
    print('Criando novo arquivo... por favor aguarde!!')
    criarArquivo(arq)
menuprincipal()

