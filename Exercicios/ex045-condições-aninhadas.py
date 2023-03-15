from random import randint
from time import  sleep
cores = {'limpa':'\033[m',
         'vermelho':'\033[1:31m',
         'amarelo':'\033[1:33m',
         'verde':'\033[1:32m'}

print('''{}HORA DE JOGAR JOKENPO!{}
{}[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA{}'''.format(cores['amarelo'], cores['limpa'], cores['vermelho'], cores['limpa']))
escolha = int(input('Faça sua escolha: '))
ia = randint(1, 3)

if escolha == 1:
    escolha = 'pedra'
elif escolha == 2:
    escolha = 'papel'
elif escolha == 3:
    escolha = 'tesoura'
else:
    print('Comando inválido!')
    exit()

if ia == 1:
    ia = 'pedra'
elif ia == 2:
    ia = 'papel'
elif ia == 3:
    ia = 'tesoura'
print('=-='*30)
print('AGORA É A HORA DA VERDADE!')
print('=-='*30)
sleep(2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('=-='*30)
if escolha == ia:
    print('SUA ESCOLHA: {} x ESCOLHA DO COMPUTADOR: {}!'.format(escolha.upper(), ia.upper()))
    print('EMPATE!')
elif escolha == 'pedra' and ia == 'papel' or escolha == 'papel' and ia == 'tesoura' or escolha == 'tesoura' and ia == 'pedra':
    print('SUA ESCOLHA: {} x ESCOLHA DO COMPUTADOR: {}!'.format(escolha.upper(), ia.upper()))
    print('VOCÊ PERDEU!')
elif escolha == 'pedra' and ia == 'tesoura' or escolha == 'papel' and ia == 'pedra' or escolha == 'papel' and ia == 'pedra':
    print('SUA ESCOLHA: {} x ESCOLHA DO COMPUTADOR: {}!'.format(escolha.upper(), ia.upper()))
    print('VOCÊ GANHOU!')
print('=-='*30)
