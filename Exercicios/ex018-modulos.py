from math import radians,sin,cos, tan
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo de {}º tem: \nSeno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}.'.format(angulo, seno, cosseno, tangente))

