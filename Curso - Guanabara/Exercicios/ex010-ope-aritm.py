n1 = float(input('Digite a quantidade de dinheiro que deseja converter: R$'))

dol = n1/5.20
euro = n1/5.52
iene = n1/0.0382489625


print('='*62)
print('Agora vamos para a conversão, mas lembre-se, quem converte não se diverte!')
print('='*62)
print('Baseado na cotação atual, você conseguirá comprar: U${:.2f}\nSe preferir comprar euro: €{:.2f}\nOu até mesmo se pensa em ir para o japão: ¥{:.2f}.'.format(dol, euro, iene))
print('='*62)
print('Boa viagem!!')
print('='*62)


