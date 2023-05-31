from datetime import datetime


def voto(nascimento):
    n = datetime.today().year - nascimento
    if n < 16:
        return 'NÃO PODE VOTAR'
    elif n >= 18 and n < 68:
        return 'VOTO OBRIGATÓRIO'
    elif n > 16 and n < 18 or n > 68:
        return 'VOTO OPCIONAL'


idade = int(input('Digite o ano de seu nascimento: '))
print(f'Com {datetime.today().year - idade} anos: {voto(idade)}')