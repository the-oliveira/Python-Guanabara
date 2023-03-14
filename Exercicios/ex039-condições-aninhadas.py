import datetime
nome = str(input('Digite o seu nome: '))
data = int(input('Você nasceu em que ano? '))
idade = datetime.date.today().year - data

if idade < 18:
    print('Olá {}, \033[1:31mainda não está na sua hora de se alistar\033[m, porém daqui {} anos você poderá se alistar!'.format(nome, 18-idade))
elif idade == 18:
    print('Olá {}, \033[1:32mestá na hora de se alistar!\033[m\nVocê completa 18 anos este ano então é hora de se alistar, boa sorte!'.format(nome))
elif idade > 18:
    print('Olá {}, você já se alistou? pois ja se passaram {} ano(s) do seu ano de alistamento!'.format(nome, idade-18))
print('Tenha um excelente dia!')
