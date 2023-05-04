lista = []
while True:
    numero = int(input('Digite um valor: '))
    if lista.count(numero) >= 1:
        print('Numero repetido, não irei adicionar!')
    else:
        lista.append(numero)
        print('Numero adicionado com sucesso!')
    contiuar = str(input('Deseja adicionar mais números? [S/N] ')).strip().upper()[0]
    while contiuar not in 'SN':
        print('Comando inválido.. Tente novamente!')
        contiuar = str(input('Deseja adicionar mais números? [S/N] ')).strip().upper()[0]
    if contiuar == 'N':
        break
lista.sort()
print(f'Você adicionou os números {lista}')

