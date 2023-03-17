import datetime

maior = 0
menor = 0
presente = datetime.date.today().year

for pessoas in range(1,8):
    ano = int(input(f'Ano de nascimento da {pessoas}ª pessoa: '))
    if presente - ano >= 21:
        maior = maior + 1
    else:
        menor = menor + 1

print(f'Ao todo {maior} são maiores de idade.')
print(f'E também tivemos {menor} menores de idade.')

