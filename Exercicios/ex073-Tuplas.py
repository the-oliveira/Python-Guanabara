tabela = 'Fluminense', 'Botafogo', 'Fortaleza', 'Palmeiras', 'Vasco', "Internacional", 'Bragantino', 'Flamengo', 'São Paulo', 'Goiás', 'Athletico-PR', 'Cruzeiro', 'Grêmio', 'Corinthians', 'Cuiabá', 'Atlético-MG', 'Santos', 'Bahia', 'Coritiba', 'América-MG'
print(tabela)
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print(f'Os Ultimos 4 colocados: {tabela[-4:]}')
print('A ordem alfabética dos times: ', end='')
print(sorted(tabela))
print('O time do Corinthians está na posição: ', end='')
print(tabela.index('Corinthians')+1)


