#dicionario['nova atriubuição'] = 'Valor do dicionario' - para adicionar novos indices no dicionario
#del dicionario['indice'] para deletar um indice
#print(variavel.values()) - ira retornar todos os valores do dicionario
#print(variavel.keys()) - ira retornar todos os indices do dicionario
#print(variavel.items()) - ira retornar tanto os values quanto os keys
#criar um laço for utilizando items, keys e values simplifica e substitui o enumerate
pessoas = {'Nome': 'Eduardo', 'sexo': 'M', 'idade': 23}
del pessoas['sexo']
pessoas['Nome'] = 'Anna'
for k, v in pessoas.items():
    print(f' {k} = {v}')
print()
time = []
jogador1 = {'nick':'Rodrix', 'lane':'Top'}
jogador2 = {'nick':'Nizzi', 'lane':'Jg'}
jogador3 = {'nick':'Ddz', 'lane':'Mid'}
jogador4 = {'nick':'Vinxs', 'lane':'Adc'}
jogador5 = {'nick':'Gu', 'lane':'Sup'}
time.append(jogador1)
time.append(jogador2)
time.append(jogador3)
time.append(jogador4)
time.append(jogador5)
for lane in time:
    for k,v in lane.items():
        print(f'{k} = {v}', end=' ')
    print()

#dicionario.copy() para copiar o conteudo para uma lista. (substituindo o [:]