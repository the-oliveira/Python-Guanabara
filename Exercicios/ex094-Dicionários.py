lista = []
mulheres = []
indice = {}
idademedia = idade = 0
while True:
    indice['Nome'] = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo not in "MF":
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    indice['Sexo'] = sexo
    idade = int(input('Idade: '))
    idademedia += idade
    indice['Idade'] = idade
    lista.append(indice.copy())
    del indice['Nome']
    del indice['Sexo']
    del indice['Idade']
    continuar = str(input('Deseja cadastrar mais alguém? [S/N] ')).upper().strip()[0]
    while continuar not in "SN":
        continuar = str(input('Comando inválido! Deseja cadastrar mais alguém? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Ao todo foram cadastradas {len(lista)} pessoas')
print(f'A média de idade foi de {idademedia/len(lista)}')
for p, d in enumerate(lista):
    if lista[p]['Sexo'] == 'F':
        mulheres.insert(lista[p]['Nome'])
        print(f'{lista[p]["Nome"]}', end=' ')

