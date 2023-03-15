reta1 = float(input('Valor da primeira reta: '))
reta2 = float(input('Valor da segunda reta: '))
reta3 = float(input('Valor da terceira reta: '))
print('=-='*25)
print('\033[1:33mANALISANDO O TRIÂNGULO\033[m')
print('=-='*25)

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('\033[1:32mOs valores de {:.2f}, {:.2f} e {:.2f} podem formar um triângulo!\033[m'.format(reta1, reta2, reta3))
else:
    print('\033[1:31mOs valores {:.2f}, {:.2f} e {:.2f} não podem formar um triângulo!\033[m'.format(reta1, reta2, reta3))

if reta1 == reta2 and reta1 == reta3 and reta2 == reta3:
    print('O triângulo formado é um \033[4:34mEquilátero\033[m.')
elif reta1 == reta2 and reta2 != reta3 and reta1 != reta3 or reta2 == reta3 and reta1 != reta2 and reta1 != reta3 or reta3 == reta1 and reta3 != reta2 and reta1 != reta2:
    print('O triângulo formado é um \033[4:34mIsósceles\033[m.')
elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
    print('O triângulo formado é um \033[4:34mEscaleno\033[m.')

