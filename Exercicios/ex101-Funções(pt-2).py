def voto(nascimento):
    """
    Programa para descobrir se o voto é Obrigatório, opcional ou não pode votar.
    :param nascimento: Ano de nascimento
    :return: Situação
    """
    from datetime import datetime
    n = datetime.today().year - nascimento
    if n < 16:
        return f'Com {n} anos: NÃO PODE VOTAR!'
    elif n >= 18 and n < 68:
        return f'Com {n} anos: O VOTO É OBRIGATÓRIO!'
    elif n >= 16 and n <= 17 or n > 65:
        return f'Com {n} anos: O VOTO É OPCIONAL!'


idade = int(input('Digite o ano de seu nascimento: '))
voto(idade)
