lista = []
calculo = input('Digite uma expressão que use parênteses: ')
lista.append(calculo)
if lista.count('(') == lista.count(')'):
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')