import datetime

maior = 0
menor = 0
presente = datetime.date.today().year

for c in range(1,8):
    ano = int(input(f'Ano de nascimento da {c}ª pessoa: '))
    if presente - ano >= 21:
        maior = maior + 1
    else:
        menor = menor + 1

print('{} são maiores de idade.'.format(maior))
print('{} são menores de idade.'.format(menor))

