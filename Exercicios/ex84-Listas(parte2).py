lista = []
dados = []
pesada = []
leve = []
total = 0
while True:
    dados.append(str(input('Digite o nome do paciente: ')))
    dados.append(int(input('Digite o peso em kg: ')))
    lista.append(dados[:])
    if dados[1] >= 70:
        pesada.append(dados[:])
    else:
        leve.append(dados[:])
    total += 1
    dados.clear()
    continuar = str(input('Deseja cadastrar mais alguma pessoa? [S/N] ')).upper().split()[0]
    while continuar not in 'SN':
        continuar = str(input('Comando inválido! Deseja cadastrar mais alguma pessoa? [S/N] ')).upper().split()[0]
    if continuar == 'N':
        break
print(f'O total de pessoas cadastradas foi: {total}')
print(f'As pessoas mais leves cadastradas foram: ', end=' ')
for p in leve:
    print(f'{p[0]} com {p[1]}kg, ', end='')
print()
print(f'As pessoas mais pesadas foram: ', end=' ')
for p in pesada:
    print(f'{p[0]} com {p[1]}kg, ',end=' ')
