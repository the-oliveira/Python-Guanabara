peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso/(altura*altura)

print('Seu peso é {} e sua altura {}, portanto seu IMC é: {:.2f}'.format(peso, altura, imc))
