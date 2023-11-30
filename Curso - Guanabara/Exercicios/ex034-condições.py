salario = float(input('Digite o seu salário: R$'))

if salario >= 1250:
    aumento = (salario*10/100) + salario
    print('Seu salário antigo era R${:.2f}\nSeu novo salário é de R${:.2f}, um aumento de 10%!!\nMeus parabéns!!'.format(salario, aumento))
else:
    aumento = (salario*15/100) + salario
    print('Seu salário antigo era de R${:.2f}\nSeu novo salário é de R${:.2f}\nMeus parabéns!!'.format(salario, aumento))
print('Continue com o excelente trabalho!')

