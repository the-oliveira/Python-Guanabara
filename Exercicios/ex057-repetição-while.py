g = ''
while g != 'M' and g != 'F':
    g = str(input('Qual o seu sexo? [M/F] ')).strip().upper()
    if g != 'M' and g != 'F':
        print('\033[1:31mComando inválido, tente novamente!\033[m')


if g == 'M':
    print('\033[1:36mSexo masculino registrado com sucesso!\033[m')
else:
    print('\033[1:35mSexo feminino registrado com sucesso!\033[m')
