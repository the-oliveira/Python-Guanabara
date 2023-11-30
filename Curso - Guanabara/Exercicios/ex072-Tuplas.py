numero = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
while True:
    escolha = int(input('Digite um número de 0 a 20: '))
    while escolha not in range(0, 21):
        escolha = int(input('Tente novamente. Digite um número de 0 a 20: '))
    print(f'O número escolhido se escreve da seguinte forma: {numero[escolha]}')
    continuar = str(input('Deseja ver outro número? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja ver outro número? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('Volte sempre!')