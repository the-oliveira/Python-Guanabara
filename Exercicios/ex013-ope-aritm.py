salario = float(input('Digite o salário do funcionário: '))
aumento = salario+(salario*15/100)

print('O salário atual do funcionário é de R${:.2f}\nO novo salário com o aumento de 15% será de: R${:.2f}'.format(salario, aumento))

