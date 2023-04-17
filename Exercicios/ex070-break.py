total = 0
maisde1k = 0
cont = 0
menor = 0
maisbarato = ''
while True:
    print('='*50)
    nomeproduto = str(input('Nome do produto: ')).strip()
    valor = float(input('Valor do produto: R$'))
    print('=' * 50)
    if valor >= 1000:
        maisde1k += 1
    if cont == 0:
        maisbarato = nomeproduto
        menor = valor
    if cont >= 1 and valor <= menor:
        maisbarato = nomeproduto
        menor = valor
    total += valor
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja comprar mais algo? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('='*50)
print(f'O valor total foi de R${total:.2f}.')
print(f'O produto mais barato foi o(a) {maisbarato}, custando R${menor:.2f}')
print(f'{maisde1k} produto(s) custaram mais de R$1000.')
print('='*50)