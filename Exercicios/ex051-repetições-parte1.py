print('Representação de uma Progressão Aritmética.')
ptermo = int(input('Digite o valor do primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = ptermo + (11 - 1) * razao
for c in range(ptermo, decimo, razao):
    print(f'{c}', end=' → ')


