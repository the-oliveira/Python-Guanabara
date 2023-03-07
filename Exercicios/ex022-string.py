nome = input('Digite o seu nome completo: ').strip()

print('Seu nome todo em maiúsculo: {}.'.format(nome.upper()))
print('Seu nome em minúsculo {}.'.format(nome.lower()))
espaco = len(nome) - (nome.count(' '))
print('Seu nome possuí ao todo {} letras.'.format(espaco))
nome = nome.split()
print('Seu primeiro nome é {} e ele possuí {} letras.'.format(nome[0], len(nome[0])))





