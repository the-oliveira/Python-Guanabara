from time import sleep
print('='*50)
print('\033[1:31:40mVamos nos preparar para a virada do ano novo!!\033[m')
print('='*50)
sleep(1)
for c in range(10, 0-1, -1):
    print('\033[1:36m', c, '\033[m')
    sleep(1)
print('\033[1:31:40mFELIZ ANO NOVO!!\033[m')
