#Erros = problemas na sintaxe do comando
#Exceções = erros no geral (não relacionados com sintaxe)
#Existe uma estrutura que se inicia com o comando try: onde você irá colocar a tentativa de uma operação, ou seja:
try:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    res = n1 / n2
#Após a tentativa (try) e a operação, temos o comando except, nele será realizado mais uma sequência de comandos caso a tentativa tenha dado erro.
#Escrever o except faz com que o usuario não receba a mensagem de erro no console, assim pode ser personalizada a mensagem que ele recebera caso dê erro
except (ValueError, TypeError):
    #Também podemos dar except especificando o erro, caso seja para mais de um, basta usar parenteses!
    print('Tivemos um problema com os tipos de dados que você digitou!')
except ZeroDivisionError:
    print('Digite um valor diferente de 0!!')
except KeyboardInterrupt:
    print('O usuário interrompeu o programa.')
except Exception as erro:
    print(f'Erro: {erro.__cause__}')
else:
    # Além do except (caso de erro) podemos colocar o else, para caso o try tenha sido realizado com sucesso!
    # else é opcional!
    print(f'O resultado deu {res}')
    print('fim!')
finally:
    # Além disso, possuí o comando finally, onde independente do try der certo ou errado, ele retornara a sequência de comandos:
    #Também é opicional!
    print('=' * 30)
    print('Finalizando o programa!')
    print('=' * 30)

# except Exception as erro:
    #Exception = cria uma variavel para o erro, assim podemos retornar o tipo na chamada do print:
    #print(f'Poxa, deu erro!! :C, o erro foi: {erro.__class__}')