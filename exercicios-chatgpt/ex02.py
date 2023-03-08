import math

produto = float(input('Digite o valor do produto: R$'))
desconto = produto*10/100
valorfinal = produto-desconto

print('O valor cheio do produto é de R${:.2f}, pague a vista e tenha 10% de desconto, pagando ao todo R${:.2f}'.format(produto, valorfinal))
