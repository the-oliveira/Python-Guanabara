lista = []
abre = fecha = 0
calculo = input('Digite uma expressão que use parênteses: ')
for p in calculo:
    if p == '(':
        abre += 1
    if p == ')':
        fecha += 1
lista.append(calculo)
if abre == fecha:
    print('Sua expressão é válida!')
    print(f'A função digitada foi: {calculo}')
else:
    print('Sua expressão não é válida!')
    print(f'A função digitada foi: {calculo}')