#lista1.append(lista2[:]) - serve para criarmos uma lista dentro de outra lista, o parametro [:] vai puxar os dados da lista2 para a lista 1
#print(lista[posição do dado][posição da informação dentro do dado], por exemplo:
#se a lista composta tiver os dados: lista1 [['Jorge', 12], 'Maria', 19]]
#Utilizando o print na lista1[0][0] iria mostrar o dado Jorge, pois é o primeiro dado e dentro deste dado esta na posição 0, se fosse [0][1], iria mostrar o número 12
# se printar apenas a lista[0] ele ira mostrar todos os dados na posição dentro da lista

teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Jorge'
teste[1] = 22
galera.append(teste[:]) #o parametro [:] cria uma cópia, se não utilizar ele ainda tera ligação com a lista depois de alterar e vai repetir os dados
print(galera)

galera2 = [[str(input('Digite um nome: ')), int(input('Digite a idade: '))], [str(input('Digite um nome: ')), int(input('Digite a idade: '))], [str(input('Digite um nome: ')), int(input('Digite a idade: '))], [str(input('Digite um nome: ')), int(input('Digite a idade: '))]]
print(galera2)
for p in galera2:
    print(f'{p[0]} tem {p[1]} anos')
