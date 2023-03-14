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
trintasalario = (salario*30/100) - salario

if valorparcela > trintasalario:
    




print('Tenha um excelente dia!!')