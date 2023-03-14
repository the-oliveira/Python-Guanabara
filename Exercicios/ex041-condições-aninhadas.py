import datetime
nome = str(input('Nome do atleta: '))
nascimento = int(input('Ano de nascimento: '))
idade = datetime.date.today().year - nascimento

if idade <= 9:
    print('O atleta {} pertence a categoria MIRIM.'.format(nome))
elif idade == 10 or idade == 11 or idade == 12 or idade == 13 or idade == 14:
    print('O atleta {} pertence a categoria INFANTIL.'.format(nome))
elif idade == 15 or idade == 16 or idade == 17 or idade == 18 or idade == 19:
    print('O atleta {} pertence a categoria JUNIOR.'.format(nome))
elif idade == 20:
    print('O atleta {} pertence a categoria SÊNIOR.'.format(nome))
elif idade >= 21:
    print('O atleta {} pertence a categoria MASTER.'.format(nome))

