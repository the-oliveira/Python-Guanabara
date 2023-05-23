#Funções são identificadas por:
#def nomedafunção ():
#se colocarmos um valor dentro dos parenteses na declaração usaremos um indice para modificar dentro de uma função
#Assim, ao utilizarmos em um print por exemplo é só colocar a função e nos parenteses colocar o que substituira o valor na função
def linhas():
    print('=' * 30)


def soma(a, b):
    print(f'O resultado de {a} + {b} é: ', end=' ')
    resultado = a + b
    print(resultado)


#while True:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    print(soma(a, b))

# existe o paremetro *, que é colocado dentro de: def função(*indice)
# o asterisco serve para empacotar dados que o usuario colocar, independente de serem 1 ou 10 informações.

def contador(*num):
    print(num)

#quando fazemos isso, utilizamos tuplas nas funções.


#assim nós utilizamos listas, que podem ser alteradas:
valores = [2, 3 , 10, 320, 20]

def dobra(lista):
    pos = 0
    while pos < len(valores):
        valores[pos] *= 2
        pos += 1

dobra(valores)
print(valores)