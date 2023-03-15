num = int(input('Digite um número inteiro: '))
print('''Escolha a base para conversão: 
[1] Binário
[2] Octal
[3] Hexadecimal''')
escolha = int(input('Sua opção: '))

if escolha > 3 or escolha < 1:
    print('Opção inválida, tente novamente!')
    exit()
elif escolha == 1:
    print('O valor {} em BINÁRIO é igual a {}.'.format(num, bin(num)))
    exit()
elif escolha == 2:
    print('O valor {} em OCTAL é igual a {}'.format(num, oct(num)))
    exit()
elif escolha == 3:
    print('O valor {} em HEXADECIMAL é igual a {}'.format(num, hex(num)))
    exit()
