def maior(*num):
    if len(num) == 0:
        print(f'O maior número da lista é 0 e foram digitados 0 numeros.')
        print()
    print('=' * 60)
    print(f'O maior número da lista é {max(num)} e foram digitados {len(num)} numeros.')
    print('=' * 60)



maior(2,3,32,2,1,1,2,3,4,4,4,1,1,2,2)
maior(3, 4, 5, 6, 1,2, 0, 3012930219031, 1)
maior()