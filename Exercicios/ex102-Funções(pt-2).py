def fatorial(n=1):
    global n1
    show = False
    for n in range(n1, 0, -1):
        if show == True:
            print(f'{n} x', end=' ')
        else:
            n1 *= n
    print(n1)


n1 = int(input('Digite um número: '))
fatorial(n1)
