nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
med = (nota1+nota2)/2

if med >= 7:
    print('\033[1:32mParabéns, você ficou com a média {:.1f} e foi aprovado!'.format(med))
    print('Boas férias!')
elif med < 5:
    print('\033[1:31mSua média foi de {}, portanto você foi reprovado! Se dedique mais no ano que vem!'.format(med))
    print('Até o ano que vem!')
else:
    print('\033[1:33mSua média foi de {}, portanto você está de recuperação. Não desanime, foi por pouco!'.format(med))
    print('Nos vemos semana que vem!')
