produto = float(input('Digite o valor do produto: R$'))
desconto = produto - (produto * 10 / 100)
prazo = produto + (produto * 5 / 100)
parcela = prazo/12
print('Valor do produto: R${:.2f}.\nValor á vista com 10% de desconto: R${:.2f}.\nValor a prazo com 5% de acréscimo: R${:.2f}, podendo ser parcelado em 12x de R${:.2f}.'.format(produto, desconto, prazo, parcela))
