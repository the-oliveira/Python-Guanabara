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
print("---Nª ----- ALUNO ----- MÉDIA")
for n, p in enumerate(alunos[0]):
    media = (alunos[1][n] + alunos[2][n]) / 2
    print(f'{n:^5}{p:^10}{media:^20.2f}')
while True:
    continuar = int(input("Deseja ver as notas de qual aluno? (999 para interromper o programa): "))
    if continuar == 999:
        break
    else:
        print(f'As notas do aluno {alunos[0][continuar]} foram: {alunos[1][continuar]} e {alunos[2][continuar]}')