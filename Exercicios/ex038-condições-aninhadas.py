n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))

if n1 > n2:
    print('O primeiro valor, que é {:.2f} é o maior valor.'.format(n1))
elif n2 > n1:
    print('O segundo valor, que é {:.2f} é o maior valor'.format(n2))
else:
    print('Os valores são iguais!')
