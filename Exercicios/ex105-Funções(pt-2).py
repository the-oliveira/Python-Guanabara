def notas(*n, sit=False):
    lista = [n]
    med = 0
    for n in lista:
        med += n
    med = med / len(lista)
    lista.sort()
    if sit == True:
        if med >= 7:
            return 'APROVADO'
        if med < 5:
            return 'REPROVADO'
        else:
            return 'RECUPERAÇÃO'
    dicionario = {'Total': len(lista), 'Maior Nota':max(lista), 'Menor nota': min(lista), 'Média': n, 'Situação': sit}



resp = notas(3, 4, 5, 6, 7)