tabela = 'Fluminense', 'Botafogo', 'Fortaleza', 'Palmeiras', 'Vasco', "Internacional", 'Bragantino', 'Flamengo', 'São Paulo', 'Goiás', 'Athletico-PR', 'Cruzeiro', 'Grêmio', 'Corinthians', 'Cuiabá', 'Atlético-MG', 'Santos', 'Bahia', 'Coritiba', 'América-MG'
print('='*50)
print(tabela)
print('='*50)
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print('='*50)
print(f'Os Ultimos 4 colocados: {tabela[-4:]}')
print('='*50)
print(f'A ordem alfabética dos times: {sorted(tabela)}')
print('='*50)
print(f'O time do Corinthians está na posição: {tabela.index("Corinthians")+1}')
print('='*50)


