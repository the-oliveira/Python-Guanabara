n1 = float(input('Digite o valor do produto em reais: '))
dc = n1*(5/100)
vf = n1-dc

print('O valor bruto do produto é de R${:.2f}.\nO valor com desconto de 5% a vista é de: R${:.2f}'.format(n1, vf))


