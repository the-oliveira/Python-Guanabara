lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    continuar = str(input('Deseja digitar mais algum valor? [S/N] ')).upper().split()[0]
    while continuar not in 'SN':
        print('Comando inválido, tente novamente!')
        continuar = str(input('Deseja digitar mais algum valor? [S/N] ')).upper().split()[0]
    if continuar == 'N':
        break
print('='*50)
print(f'A lista completa ficou desta forma: {lista}')
print(f'Os números pares formaram esta outra lista: {par}')
print(f'Já os números impares formaram esta: {impar}')
print('Volte sempre!')
print('='*50)
