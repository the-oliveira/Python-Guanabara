def notas(*n, sit=False):
    """
    Programa para avaliar a situação de um conjunto de notas.
    :param n: Recebe várias notas
    :param sit: [Opcional]Caso queira mostrar a situação final colocar sit = True, por padrão sit = False.
    :return: Dicionário com informações de notas, maior nota, menor nota, média e situação final(opcional)
    """
    lista = [n]
    final = ''
    med = 0
    for n in lista[0]:
        med += n
    med = med / len(lista[0])
    if med > 7:
        final = 'APROVADO'
    elif med < 5:
        final = 'REPROVADO'
    elif 5 < med < 7:
        final = 'RECUPERAÇÃO'
    if sit == False:
        return {'Total': len(lista[0]), 'Maior Nota': max(lista[0]), 'Menor nota': min(lista[0]), 'Média': med}
    else:
        return {'Total': len(lista[0]), 'Maior Nota':max(lista[0]), 'Menor nota': min(lista[0]), 'Média': med, 'Situação': final}



resp = notas(5.5, 22.5, 1.5, sit=True)
print(resp)
help(notas)
