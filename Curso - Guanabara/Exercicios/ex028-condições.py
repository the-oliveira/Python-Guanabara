from random import randint
from time import sleep

sort = randint(0, 5)
print('='*60)
print('Irei pensar em um número de 0 a 5, tente advinhar!')
print('='*60)
n1 = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if n1 == sort:
    print('O computador escolheu o número {}\nVocê foi sábio e ganhou, PARABÉNS!'.format(sort))
else:
    print('O computador escolheu o número {} e você {}.\nVOCÊ PERDEU!'.format(sort, n1))
print('='*60)
print('---FIM DE JOGO---')
print('='*60)


