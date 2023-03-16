tabuada = int(input('Qual tabuada deseja saber? '))
for c in range(1,10+1):
    m = tabuada * c
    print('{} x {} = {}'.format(tabuada, c, m))
