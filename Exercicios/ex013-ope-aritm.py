salario = float(input('Digite o salário do funcionário: '))
aumento = salario*(15/100)
vf = salario+aumento

print('O salário atual do funcionário é de R${:.2f}\nO novo salário com o aumento de 15% será de: R${:.2f}'.format(salario, vf))
