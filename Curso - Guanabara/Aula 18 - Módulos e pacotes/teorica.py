#Modularização facilita manutenção do código
#Codigo fica mais organizado e mais legível
#Pode utilizar os códigos do modulo em outros programas
#Para chamar uma modularização basta utilizar o comando import ou from para puxar um comando específico.
#Pacotes podem unir varios modulos para tornar mais organizado quando as modulações começam a ficar cheias de códigos, assim é possível filtrar por tópicos
#Também é importado pelo comando import.
#Pacotes são separados por pastas, portanto, se criarmos uma pasta chamada uteis, e dentro dela outras subpastas com categorias diferentes e modulações diferentes, isso é um pacote.
#No pycharm, basta clicar com o botão direito e criar um novo arquivo como pacote e criar outros sub pacotes dentro do principal.
#Para criar o modulo basta colocar o código no ___init___.py do pacote
from uteis import numeros
n = int(input('Digite um número> '))
fat = numeros.fatorial(n)
print(f'O fatorial de {n} é {fat}')
print(f'O dobro de {n} é {numeros.dobro(n)}')
