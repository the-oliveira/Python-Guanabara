lista = []
mulheres = []
indice = {}
idademedia = idade = 0
while True:
    indice['Nome'] = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo not in "MF":
        print('Comando inválido! Digite apenas M ou F')
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    indice['Sexo'] = sexo
    idade = int(input('Idade: '))
    idademedia += idade
    indice['Idade'] = idade
    lista.append(indice.copy())
    indice.clear()
    continuar = str(input('Deseja cadastrar mais alguém? [S/N] ')).upper().strip()[0]
    while continuar not in "SN":
        continuar = str(input('Comando inválido! Deseja cadastrar mais alguém? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('='*40)
print(f'Ao todo foram cadastradas {len(lista)} pessoas')
print(f'A média de idade foi de {idademedia/len(lista):.2f}')
print('As mulheres cadastradas foram: ', end=' ')
for p in lista:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end=' ')
print()
print('Lista de pessoas acima da média de idade: ')
for p in lista:
    if p['Idade'] > idademedia/len(lista):
        print(f'   - {p["Nome"]} com {p["Idade"]} anos')
print('Fim do programa!')
