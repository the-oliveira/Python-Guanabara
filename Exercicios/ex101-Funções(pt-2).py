from datetime import datetime


def voto(nascimento):
    n = datetime.today().year - nascimento
    if n < 16:
        return print(f'Com {n} anos: NÃO PODE VOTAR!')
    elif n >= 18 and n < 68:
        return print(f'Com {n} anos: O VOTO É OBRIGATÓRIO!')
    elif n > 16 and n < 18 or n > 68:
        return print(f'Com {n} anos: O VOTO É OPCIONAL!')


idade = int(input('Digite o ano de seu nascimento: '))
voto(idade)
