from time import sleep

def contador(inicio, fim, passo):
    print('=' * 40)
    print(f'Vamos contar de {inicio} até {fim} de {passo} em {passo}')
    print('=' * 40)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += passo
        print()
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= passo
        print()


contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
contador(inicio=int(input('Inicio: ')), fim=int(input('Até que número? ')), passo=int(input('De quanto em quanto? ')))
