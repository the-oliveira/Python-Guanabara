from random import randint
tentativas = 1
rand = randint(0, 10)
n = int(input('Advinhe o número que o PC pensou de 1 a 10: '))
while n != rand:
    if n > rand:
        print('Talvez um pouco menor...')
    if n < rand:
        print('Talvez um pouco maior...')
    n = int(input('Tente novamente: '))
    tentativas += 1

print(f'Você finalmente acertou! O número era {rand} e você acertou em {tentativas} tentativas.')