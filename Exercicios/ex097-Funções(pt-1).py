def linhas(txt):
    print('=' * len(txt))
    print(txt)
    print('=' * len(txt))


while True:
    linhas(txt=str(input('Digite um texto: ')))