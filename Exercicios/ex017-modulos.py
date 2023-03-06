from math import hypot

catetoposto = float(input('Digite o valor do cateto oposto: '))
catetoadj = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(catetoposto, catetoadj)

print('O triângulo retângulo possui o cateto oposto = {}, o cateto adjacente = {} e a sua hipotenusa = {:.2f}'.format(catetoposto, catetoadj, hipotenusa))
