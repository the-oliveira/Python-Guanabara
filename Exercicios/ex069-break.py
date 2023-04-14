mais18 = 0
homens = 0
mulheres20 = 0
while True:
    print('='*20)
    print('CADASTRO DE CLIENTES.')
    print('=' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    if idade >= 18:
        mais18 += 1
    if idade <= 20 and sexo == 'F':
        mulheres20 += 1
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('=' * 80)
print(f'Dentre os clientes cadastrados {mais18} são maiores de 18 anos, tanto do sexo masculino quanto feminino.')
print(f'Sendo ao todo {mulheres20} mulher(es) menor(es) de 20 anos.')
print(f'E também consta nos registros {homens} homen(s) cadastrados.')
print('=' * 80)