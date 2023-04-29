tabela = 'Fluminense', 'Botafogo', 'Fortaleza', 'Palmeiras', 'Vasco', "Internacional", 'Bragantino', 'Flamengo', 'São Paulo', 'Goiás', 'Athletico-PR', 'Cruzeiro', 'Grêmio', 'Corinthians', 'Cuiabá', 'Atlético-MG', 'Santos', 'Bahia', 'Coritiba', 'América-MG'
print(tabela)
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print(f'Os Ultimos 4 colocados: {tabela[-4:]}')
print('A ordem alfabética dos times: ', end='')
print(sorted(tabela))
time = str(input('Quer saber a posição de que time? ')).strip().capitalize()
print(f'O time do {time} está na posição: ', end='')
print(tabela.index(time)+1)


