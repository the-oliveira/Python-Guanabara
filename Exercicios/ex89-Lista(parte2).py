alunos = [[], [], []]
media = 0
while True:
    alunos[0].append(str(input('Digite o nome do aluno: ')))
    alunos[1].append(float(input('Digite a primeira nota: ')))
    alunos[2].append(float(input('Digite a segunda nota: ')))
    continuar = str(input('Deseja cadastrar mais um aluno? [S/N] ')).upper().split()[0]
    while continuar not in 'SN':
        continuar = str(input('Comando inválido! Digite novamente: [S/N] ')).upper().split()[0]
    if continuar == 'N':
        break
for p in range(0, len(alunos[0])):
    for n1 in alunos[1]:
        for n2 in alunos[2]:
            print(f'{alunos[0][p]} ', end=' ')
            media = (n1 + n2) / 2
            print(f'Média do aluno: {media}')
