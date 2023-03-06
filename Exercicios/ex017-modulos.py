import math

catetoposto = float(input('Digite o valor do cateto oposto: '))
catetoadj = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.sqrt(catetoadj*catetoadj) + (catetoposto*catetoposto)

print('O triângulo retângulo possui o cateto oposto = {}, o cateto adjacente = {} e a sua hipotenusa = {}'.format(catetoposto, catetoadj, hipotenusa))
