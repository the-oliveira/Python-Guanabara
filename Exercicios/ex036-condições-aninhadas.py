nome = str(input('Digite o seu nome: '))
casa = float(input('Qual o valor da casa que deseja financiar? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Deseja pagar a casa em quantos anos? '))
cores = {'vermelho':'\033[1:31m',
         'limpa':'\033[m',
         'verde':'\033[1:32m'
         }
parcelas = anos*12
valorparcela = casa/parcelas

if valorparcela < salario*30/100:
    print('Parabéns, o seu financiamento foi {}aprovado!{}'.format(cores['verde'], cores['limpa']))
    print('Você ira comprar uma casa de R${:.2f} em {}x de R${:.2f}'.format(casa, parcelas, valorparcela))
else:
    print('{}Financiamento negado{}\nAs parcelas excederam o valor de 30% do seu salário atual.'.format(cores['vermelho'], cores['limpa']))
print('Tenha um excelente dia {}!'.format(nome))

