from datetime import datetime


def voto(nascimento):
    """
    Programa para descobrir se o voto é Obrigatório, opcional ou não pode votar.
    :param nascimento: Ano de nascimento
    :return: Situação
    """
    n = datetime.today().year - nascimento
    if n < 16:
        return print(f'Com {n} anos: NÃO PODE VOTAR!')
    elif n >= 18 and n < 68:
        return print(f'Com {n} anos: O VOTO É OBRIGATÓRIO!')
    elif n >= 16 and n <= 17 or n > 68:
        return print(f'Com {n} anos: O VOTO É OPCIONAL!')


idade = int(input('Digite o ano de seu nascimento: '))
voto(idade)
