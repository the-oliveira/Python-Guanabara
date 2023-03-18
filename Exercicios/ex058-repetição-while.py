from random import randint
tentativas = 1
rand = randint(0, 10)
n = int(input('Advinhe o número que o PC pensou de 1 a 10: '))
while n != rand:
    n = int(input('Você errou, tente novamente: '))
    tentativas += 1

print(f'Você finalmente acertou! O número era {rand} e você acertou em {tentativas} tentativas.')