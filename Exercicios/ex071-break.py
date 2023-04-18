sacar = int(input('Quanto deseja sacar? '))
valor = sacar
totalced = 0
cedatual = 50
while True:
    if valor >= cedatual:
        valor -= cedatual
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${cedatual}')
        if cedatual == 50:
            cedatual = 20
        elif cedatual == 20:
            cedatual = 10
        elif cedatual == 10:
            cedatual = 1
        if valor == 0:
            break