dias = int(input('Quantos dias irá alugar o carro: '))
km = float(input('Quantos km rodados: '))
valordia = dias*60
valorkm = km*0.15

print('O valor total a ser pago é de: R${:.2f}'.format(valordia+valorkm))
