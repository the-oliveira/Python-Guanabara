numeros = 0
n1 = 0
numero = 0
while numero != 999:
    numeros += 1
    numero = int(input('Digite um número (digite 999 se deseja finalizar a soma): '))
    if numero == 999:
        n1 -= 999
        numeros -= 1
    n1 = numero + n1

print(f'Você digitou {numeros} numeros e a soma de todos eles é igual a {n1}')
