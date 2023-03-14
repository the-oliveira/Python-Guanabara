n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

ad = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
exp = n1 ** n2
divint = n1 // n2
restdiv = n1 % n2


print('Adição: {}\nSubtração: {}\nMultiplicação: {}\nDivisão: {}\nPotência: {}\nDivisão inteira: {}\nResto da divisão: {}.'.format(ad, sub, mult, div, exp, divint, restdiv))
