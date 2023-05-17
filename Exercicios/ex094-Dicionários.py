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
print('='*40)
print(f'Ao todo foram cadastradas {len(lista)} pessoas')
print(f'A média de idade foi de {idademedia/len(lista)}')
print('As mulheres cadastradas foram: ', end=' ')
for p, d in enumerate(lista):
    if lista[p]['Sexo'] == 'F':
        print(f'{lista[p]["Nome"]} ', end=' ')
print()
print('Lista de pessoas acima da média de idade: ')
for p, d in enumerate(lista):
    if lista[p]['Idade'] >= idademedia/len(lista):
        print(f'{d}', end=' ')
    print()
print('Fim do programa!')
