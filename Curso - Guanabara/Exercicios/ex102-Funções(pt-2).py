def fatorial(n=1, show=False):
    """
    Programa para calcular o Fatorial de um número
    :param n: Número que iremos calcular o Fatorial
    :param show: Comando OPCIONAL, mostra ou não a formula da conta
    :return:Fatorial de N
    """
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(f'{c}', end=' ')
            if c > 1:
                print(f' x ', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f


n = int(input('Digite um número para ver seu fatorial: '))
mostrar = str(input('Deseja ver a formula completa? [S/N] ')).upper()[0]
if mostrar == 'S':
    mostrar = True
else:
    mostrar = False
print(fatorial(n, mostrar))
help(fatorial)