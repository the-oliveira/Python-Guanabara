med = 0
vinte = 0
for c in range(0,4):
    nome = str(input('Qual o seu nome? '))
    idade = int(input('Qual a sua idade? '))
    med += idade
    sexo = str(input('Qual o seu sexo? ')).lower()
    if sexo == 'feminino' and idade > 20:
        vinte += 1

print('A média de idade do grupo é de: {:.1f}'.format(med/4))
print('O número de mulheres com menos de 20 anos é de: {}'.format(vinte))