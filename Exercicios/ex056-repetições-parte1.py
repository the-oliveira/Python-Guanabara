med = 0
vinte = 0
lista = []
nomelist = []
for c in range(1,5):
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    med += idade
    sexo = str(input('SEXO [M/F]: ')).lower().strip()

    if sexo == 'f' and idade > 20:
        vinte = vinte + 1
    elif sexo == 'm':
        lista += [idade]
        nomelist += [nome]
    print('='*10)

lista.sort()
print(lista)
print(nomelist)
print('A média de idade do grupo é de: {:.1f}'.format(med/4))
print('O número de mulheres com menos de 20 anos é de: {}'.format(vinte))
