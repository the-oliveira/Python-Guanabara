genero = ''
while genero != 'M' and genero != 'F':
    genero = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
    if genero != 'M' and genero != 'F':
        print('\033[1:31mComando inválido, tente novamente!\033[m')


if genero == 'M':
    print('\033[1:36mSexo masculino registrado com sucesso!\033[m')
else:
    print('\033[1:35mSexo feminino registrado com sucesso!\033[m')
