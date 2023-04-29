numero = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
escolha = int(input('Digite um número de 0 a 20: '))
while escolha not in range(0, 21):
    escolha = int(input('Tente novamente. Digite um número de 0 a 20: '))
print(f'O número escolhido se escreve da seguinte forma: {numero[escolha]}')
