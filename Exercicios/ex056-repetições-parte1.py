med = 0
vinte = 0
for c in range(0,4):
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    med += idade
    sexo = str(input('SEXO: ')).lower()
    if sexo == 'feminino' and idade > 20:
        vinte = vinte + 1
    print('='*10)

print('A média de idade do grupo é de: {:.1f}'.format(med/4))
print('O número de mulheres com menos de 20 anos é de: {}'.format(vinte))
