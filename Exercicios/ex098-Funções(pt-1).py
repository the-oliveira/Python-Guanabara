def contador():
    inicio = int(input('Inicio: '))
    fim = int(input('Final: '))
    passo = int(input('Passo: '))
    if passo == 0:
        passo = 1
    cont = 0
    while True:
        if cont == 0:
            for a in range(1, 10, 1):
                print(f'{a} ', end=' ')
        if cont == 1:
            for b in range(10, 0, 2):
                print(f'{b} ', end=' ')
        if cont == 2:
            for c in range(inicio, fim, passo):
                print(f'{c} ', end=' ')
        if cont == 3:
            break
        cont += 1


contador()