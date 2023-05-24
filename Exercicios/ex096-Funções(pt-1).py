def area(l, a):
    print('='*30)
    print(f'{"Calculando Terrenos!":^30}')
    print('=' * 30)
    area = l * a
    print(f'O terreno {l} x {a}m possui {area}m² de área!')


print(area(l=float(input('LARGURA (m)')), a= float(input('Comprimento (m): '))))