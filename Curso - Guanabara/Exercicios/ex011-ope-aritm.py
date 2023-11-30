l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l*a

print('A parede possuí {}x{}m, sendo assim, sua área é de: {:.2f}m²'.format(l, a, area))
print('A quantidade de tinta para pinta-la é de: {:.2f}l.'.format(area/2))
