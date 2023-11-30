#EXEMPLO DO COMANDO: \033[XX:XX:XXm

#primeiro valor após o '[' é referente ao estilo, possuindo principalmente o 0(nenhum) 1(bold) 4(underline) e 7(negativo)
#Segundo valor, após o estilo, é o da cor do texto: 30(preto) 31(vermelho) 32(verde) 33(amarelo) 34(azul) 35(magenta) 36(ciano) 37(cinza) e 97(branco)
#Terceiro valor, cor do background: 40(preto) 41(vermelho) 42(verde) 43(amarelo) 44(azul) 45(magenta) 46(ciano) 47(cinza) 107(branco)
nome = str(input('Digite o seu nome: '))
cores = {'limpa':'\033[m',
         'azul':'\033[1;34;40m',
         'ciano':'\033[4;36;40m'}

print('{}Olá! {}'.format(cores['azul'], cores['limpa']))
print('Prazer em te conhecer {}{}{}!!'.format(cores['ciano'], nome, cores['limpa']))

