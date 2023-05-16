from datetime import datetime
dados = {}
dados['nome'] = str(input('Digite seu nome: '))
nascimento = int(input('Ano de nascimento: '))
nascimento = datetime.today().year - nascimento
dados['idade'] = nascimento
ctps = int(input('Digite o número da sua carteira de trabalho: (000 se não houver)'))
if ctps != 000:
    dados['ctps'] = ctps
    dados['salário'] = float(input('Digite o seu salário atual ou ultimo salário: R$'))
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['aposentadoria'] = dados['Contratação'] + 32
else:
    print('Talvez seja o momento de tirar sua carteira!')
print(dados)
for k, v in dados.items():
    print(f'{k} {v}')
