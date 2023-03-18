c = 1
par = 0
impar = 0
while c != 0:
    c = float(input('Digite um número: '))
    if c != 0:
        if c % 2 == 0:
            par += 1
        else:
            impar +=1

print(f'Foram digitados {par} valores pares e {impar} valores impares.')
