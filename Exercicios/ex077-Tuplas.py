palavras = 'Abraço', 'Jorge', 'Marfim', 'Corinthians', 'Campeao', 'Alagoas'
for p in palavras:
    print(f'\nNa palavra {p} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end='')

