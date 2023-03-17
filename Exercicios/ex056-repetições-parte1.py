med = 0
vinte = 0
maioridade = 0
nomevelho = ''

for c in range(1,5):
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    med += idade
    sexo = str(input('SEXO [M/F]: ')).lower().strip()

    if sexo == 'f' and idade < 20:
        vinte = vinte + 1
    elif sexo == 'm' and c == 1:
        maioridade = idade
        nomevelho = nome
    if sexo == 'm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    print('='*10)

med = med/4
print(f'O nome do homem mais velho é {nomevelho} e a sua idade é {maioridade:.0f}')
print(f'A média de idade do grupo é de: {med:.1f}')
print(f'O grupo possui {vinte} mulher(es) com menos de 20 anos.')
