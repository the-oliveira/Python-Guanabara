total = 0
maisde1k = 0
cont = 0
menor = 0
maisbarato = ''
while True:
    nomeproduto = str(input('Nome do produto: ')).strip()
    valor = float(input('Valor do produto: R$'))
    if valor >= 1000:
        maisde1k += 1
    if cont == 0:
        maisbarato = nomeproduto
        menor = valor
    if valor <= menor:
        maisbarato = nomeproduto
        menor = valor
    total += valor
    continuar = str(input('Deseja finalizar a compra? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O valor total gaasto na compra foi de R${total:.2f}.')
print(f'O produto mais barato foi o {maisbarato}, custando R${menor:.2f}')
print(f'{maisde1k} custaram mais de R$1000.')