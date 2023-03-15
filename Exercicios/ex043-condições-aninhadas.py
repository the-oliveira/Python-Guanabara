peso = float(input('Peso (em KG): '))
altura = float(input('Altura (em metros): '))
imc = peso/(altura * altura)

if imc < 18.5:
    print('Seu IMC é:{:.1f} portanto você está abaixo do peso '.format(imc))
elif imc >= 18.5 or imc < 25:
    print('Seu IMC é:{:.1f} portanto você está no peso ideal '.format(imc))
elif imc >= 25 or imc < 30:
    print('Seu IMC é:{:.1f} portanto você está sobrepeso '.format(imc))
elif imc >= 30 or imc < 40:
    print('Seu IMC é:{:.1f} portanto você está com obesidade '.format(imc))
elif imc >= 40:
    print('Seu IMC é:{:.1f} portanto você está com obesidade mórbida '.format(imc))
    