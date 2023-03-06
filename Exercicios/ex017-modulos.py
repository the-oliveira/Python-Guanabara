import math

catetoposto = float(input('Digite o valor do cateto oposto: '))
catetoadj = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.sqrt((catetoadj**2) + (catetoposto**2))

print('O triângulo retângulo possui o cateto oposto = {}, o cateto adjacente = {} e a sua hipotenusa = {:.2f}'.format(catetoposto, catetoadj, hipotenusa))
