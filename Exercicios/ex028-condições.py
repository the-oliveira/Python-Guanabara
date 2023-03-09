import random
n1 = int(input('Tente advinhar o número em que eu pensei de 0 a 5: '))
n2 = [0, 1, 2, 3, 4, 5]
sort = random.choice(n2)

if n1 == sort:
    print('O computador escolheu o número {}\nVocê foi sábio e ganhou, PARABÉNS!'.format(sort))
else:
    print('O computador escolheu o número {} e você {}.\nVOCÊ PERDEU!'.format(sort, n1))
print('---FIM DE JOGO---')



