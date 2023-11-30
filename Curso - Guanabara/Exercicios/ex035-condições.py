print('=-='*20)
print('Formando Triângulos!')
print('=-='*20)

n1 = float(input('Valor da primeira reta: '))
n2 = float(input('Valor da segunda reta: '))
n3 = float(input('Valor da terceira reta: '))


if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('O segmento pode formar um triângulo!!')
else:
    print('O segmento não pode formar um triângulo!!')


