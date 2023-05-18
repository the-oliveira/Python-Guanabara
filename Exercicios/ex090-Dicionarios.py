alunos = {'Nome':str(input("Nome do Aluno: ")), 'Média':float(input("Média do Aluno: "))}
if alunos['Média'] >= 7:
    alunos['Situação'] = 'Aprovado'
else:
    alunos['Situação'] = 'Reprovado'
for k, v in alunos.items():
    print(f'{k} = {v}')
