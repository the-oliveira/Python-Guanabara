alunos = {'Nome':str(input("Nome do Aluno: ")), 'Média':float(input("Média do Aluno: "))}
if alunos['Média'] >= 7:
    alunos['Situação'] = 'Aprovado'
elif alunos['Média'] > 5 < 7:
    alunos['Situação'] = 'Recuperação'
else:
    alunos['Situação'] = 'Reprovado'
for k, v in alunos.items():
    print(f'{k} = {v}')
