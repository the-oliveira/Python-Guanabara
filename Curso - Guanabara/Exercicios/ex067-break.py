cont = 1
tabuada = int(input('Digite a tabuada que deseja ver: '))
while True:
    mult = tabuada*cont
    print(f'{tabuada} x {cont} = {mult}')
    cont += 1
    if cont == 11:
        cont = 1
        tabuada = int(input('Digite a tabuada que deseja ver: '))
    if tabuada < 0:
        break
print('Fim do programa! Volte sempre!')
