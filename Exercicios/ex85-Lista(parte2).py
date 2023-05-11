numeros = [[], []]
dados = []
for c in range(0, 7):
    dados.append(int(input(f'Digite o {c+1}ª valor: ')))
    if dados[0] % 2 == 0:
        numeros[0].append(dados[:])
        numeros[0].sort()
    else:
        numeros[1].append(dados[:])
        numeros[1].sort()
    dados.clear()
print(f'Os números pares digitados foram {numeros[0]}')
print(f'Os números impares digitados foram {numeros[1]}')