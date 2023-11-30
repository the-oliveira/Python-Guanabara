from random import randint
random = randint(1,10)
num = int(input('Tente adivinhar o número de 1 a 10: '))
tentativas = 0
while num != random:
    num = int(input('Você errou, tente novamente: '))
    tentativas += 1
    if num == random:
        print(f"Parabéns, você acertou, o número era {random} e você acertou em {tentativas} tentativas!")
