from unidecode import unidecode

frase = str(input('Digite uma frase: ')).strip()
sem_acento = unidecode(frase).lower()

print('Na frase: {}, a letra *a* foi utilizada {} vezes.'.format(frase, sem_acento.count('a')))
