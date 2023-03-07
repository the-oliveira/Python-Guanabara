from unidecode import unidecode
com_acento = input('Digite uma frase: ').strip().lower()
frase = unidecode(com_acento)

print('Quantas vezes a letra A foi utilizada na sua frase: {}.'.format(frase.count('a')))
print('A primeira posição da letra A é: {}'.format(frase.find('a', 0)))
print('A ultima posição da letra A é: {}'.format(frase.find('a', -1)))
