from time import sleep
lista = []
dados = []
leve = pesada = 0
while True:
    dados.append(str(input('Digite o nome do paciente: ')))
    dados.append(float(input('Digite o peso em kg: ')))
    if len(lista) == 0:
        leve = pesada = dados[1]
    else:
        if dados[1] > pesada:
            pesada = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    lista.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja cadastrar mais alguma pessoa? [S/N] ')).upper().split()[0]
    while continuar not in 'SN':
        continuar = str(input('Comando inválido! Deseja cadastrar mais alguma pessoa? [S/N] ')).upper().split()[0]
    if continuar == 'N':
        break
print(f'O total de pessoas cadastradas foi: {len(lista)}')
print(f'O peso mais leve encontrado foi {leve}, pertecendo ao(a) ', end=' ')
for p in lista:
    if p[1] == leve:
        print(f'[{p[0]}] ', end=' ')
print()
print(f'O maior peso cadastrado foi {pesada}, pertecendo ao(a) ', end=' ')
for p in lista:
    if p[1] == pesada:
        print(f'[{p[0]}] ', end=' ')
