frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1,-1):
    inverso += junto[letra]

if inverso == junto:
    print(f'A frase {junto} ao contrario fica {inverso}\nESSA FRASE FORMOU UM PALÍNDROMO!')
else:
    print(f'A frase {junto} ao contrario fica {inverso}\nNÃO FORMOU UM PALÍNDROMO!')

