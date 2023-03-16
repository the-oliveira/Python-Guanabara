tabuada = int(input('Qual tabuada deseja saber? '))
print('*'*30)
for c in range(1,10+1):
    m = tabuada * c
    print('{} x {:2} = {}'.format(tabuada, c, m))
print('*'*30)