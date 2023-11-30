import datetime
nome = str(input('Digite o seu nome: '))
sexo = str(input('Qual o seu sexo? '))
sexolow = sexo.lower()
if sexolow == 'feminino':
    print('Você não precisa se alistar obrigatóriamente!')
    print('Tenha um excelente dia!')
    exit()
data = int(input('Você nasceu em que ano? '))
idade = datetime.date.today().year - data

if idade < 18:
    print('Olá {}, \033[1:31mainda não está na sua hora de se alistar\033[m, daqui {} anos você poderá se alistar!\nVocê irá se alistar no ano de {}'.format(nome, 18-idade, data+18))
elif idade == 18:
    print('Olá {}, \033[1:32mestá na hora de se alistar!\033[m\nVocê completa 18 anos este ano, boa sorte!'.format(nome))
elif idade > 18:
    print('Olá {}, já passaram {} ano(s) do seu ano de alistamento!\nSeu alistamento foi no ano de {}.'.format(nome, idade-18, data+18))
print('Tenha um excelente dia!')
