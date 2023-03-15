produto = float(input('Digite o valor do produto: R$'))
print('''O produto possui o valor de R${:.2f}, você pode escolher entre:
[1] Pagar á vista no dinheiro ou cheque com 10% de desconto (digite 1).
[2] Á vista no cartão de crédito com 5% de desconto (digite 2).
[3] Em 2x no cartão com o preço normal (digite 3).
[4] Em 3x ou mais no cartão com 20% de juros (digite 4).'''.format(produto))
pagamento = int(input('Escolha a forma de pagamento (1-4): '))

if pagamento == 1:
    print('Valor do produto: R${:.2f} será pago a vista e com 10% de deconto no dinheiro ou cheque, portanto o novo valor do produto é de R${:.2f}'.format(produto, produto - (produto * 10/100)))
elif pagamento == 2:
    print('Valor do produto: R${:.2f} e será pago á vista no cartão de crédito, portanto terá 5% de desconto, seu novo valor é R${:.2f}'.format(produto, produto - (produto*5/100)))
elif pagamento == 3:
    print('Valor do produto: R${:.2f} e será pago em 2x no cartão, portanto seu valor será o mesmo com duas parcelas de R${:.2f}'.format(produto, produto/2))
elif pagamento == 4:
    parcelas = int(input('Digite o número de parcelas em até 12x: '))
    if parcelas > 12:
        print('Número de parcelas inválida, tente novamente.')
        exit()
    else:
        juros = produto + (produto * 20/100)
        parcelasvalor = juros / parcelas
        print('Valor do produto: R${:.2f}, pagando em {:.0f}x de R${:.2f}, com o valor total de R${:.2f}. '.format(produto, parcelas, parcelasvalor, juros))
