def area(l, c):
    print()
    area = l * c
    print(f'O terreno {l} x {c}m possui {area}m² de área!')


print('='*30)
print(f'{"Calculando Terrenos!":^30}')
print('=' * 30)
area(l=float(input('LARGURA (m): ')), c=float(input('Comprimento (m): ')))