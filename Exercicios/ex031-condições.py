km = int(input('Digite a distância em km do seu destino: '))
longa = 0.45 * km
curta = 0.5 * km
if km <= 200:
    print('Sua viagem terá {}Km, portanto custará R${:.2f}'.format(km, curta))
else:
    print('Sua viagem terá {}km, portanto custará R${:.2f}'.format(km, longa))
print('Boa viagem!')
