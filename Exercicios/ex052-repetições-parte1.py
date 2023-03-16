for c in range(1,10):
    n = int(input('Digite um número: '))
    if n > 1 and n / n == 1:
        print('O número é primo.')
    else:
        print('O número não é primo.')