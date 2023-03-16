n = 0
for c in range(0, 50):
    n = c + 1
    if n % 2 == 0:
        print('\033[1:32m{} é par\033[m'.format(n))
    else:
        print('\033[1:31m{} é impar\033[m'.format(n))
print('Fim')
