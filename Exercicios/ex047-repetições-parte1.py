n = 0
for c in range(0, 50):
    n = c + 1
    if n % 2 == 0:
        print('{} é par'.format(n))
    else:
        print('{} é impar'.format(n))
print('Fim')
