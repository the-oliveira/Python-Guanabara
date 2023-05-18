from datetime import datetime
dados = {}
dados['Nome'] = str(input('Digite seu nome: '))
nascimento = int(input('Ano de nascimento: '))
idade = datetime.now().year - nascimento
dados['Idade'] = idade
ctps = int(input('Digite o número da sua carteira de trabalho: (0 se não houver)'))
if ctps != 0:
    dados['CTPS'] = ctps
    dados['Salário'] = float(input('Digite o seu salário atual ou ultimo salário: R$'))
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Aposentadoria'] = idade + 32
else:
    dados['Situação'] = 'Não tem CTPS'
for k, v in dados.items():
    print(f'   - {k}: {v}')
