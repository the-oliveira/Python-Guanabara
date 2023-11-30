nome = input('Digite seu nome completo: ').strip()
silva = nome.lower().split()
print('Seu nome tem Silva? {}'.format('silva' in silva))
