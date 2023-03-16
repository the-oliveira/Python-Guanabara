import datetime

maior = 0
menor = 0
presente = datetime.date.today().year

for c in range(0,7):
    ano = int(input('Ano de nascimento: '))
    if presente - ano >= 21:
        maior = maior + 1
    else:
        menor = menor + 1

print('{} são maiores de idade.'.format(maior))
print('{} são menores de idade.'.format(menor))

