produtos = 'Mangá', 9.99, 'Livro', 23.50, 'Teclado', 234.99, 'Mouse', 99.99, 'Mousepad', 34.50
print('-'*50)
print('LISTAGEM DE PRODUTOS')
print('-'*50)
for produto in range (0, len(produtos)):
    if produto % 2 == 0:
        print(f'{produtos[produto]:.<30}',end= '')
    else:
        print(f'R${produtos[produto]:>8}')
print('-'*50)

