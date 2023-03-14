nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
if media >=5:
    print('Parabéns sua média foi {:.2f} e você foi aprovado!!'.format(media))
    print('Aproveite a formatura!')
else:
    print('Que pena, sua média foi {:.2f} e você não foi aprovado.'.format(media))
    print('Nos vemos novamente no próximo ano!')
