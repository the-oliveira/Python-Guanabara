def contador(inicio, fim, passo):
    print(f'Vamos contar de {inicio} até {fim} de {passo} em {passo}')
    cont = inicio
    while cont <= fim:
        print(f'{cont}', end=' ')
        cont += passo
    print()


contador(1, 10, 1)
contador(10, 0, 2)
contador(inicio=int(input('Inicio: ')), fim=int(input('Até que número? ')), passo=int(input('De quanto em quanto? ')))