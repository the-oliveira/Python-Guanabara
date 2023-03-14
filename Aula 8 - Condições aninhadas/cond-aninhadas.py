nome = str(input('Qual o seu nome? '))

if nome == 'Eduardo':
    print('Você tem um belo nome!')
elif nome == 'Anna':
    print('Você tem um nome lindo!')
elif nome == 'Kaue':
    print('Você é calvo')
elif nome == 'Gustavo':
    print('Você é careca')
else:
    print('Seu nome é comum!')
print('Tenha um excelente dia, \033[1:61:40m{}\033[m!'.format(nome))
