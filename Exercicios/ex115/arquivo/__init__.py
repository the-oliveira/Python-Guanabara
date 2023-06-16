def arquivoExiste(nome):
    try:
        #comando open = ele irá abrir um arquivo dentro do diretório.
        #o 'rt' após o nome do arquivo significa "read" e "Text", ou seja, verifica o arquivo se é possível ler ele.
        #close = fecha o arquivo após abri-lo.
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        #FileNotFoundError = erro caso o arquivo não exista.
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        #wt = escrever um arquivo de texto
        #wt+ = o "+" significa, caso não exista o arquivo, crie um.
        a = open(nome, "wt+")
        a.close()
    except:
        print(f'Houve um erro ao criar o arquivo {nome}')
    else:
        print(f'Arquivo {nome} criado com sucesso!')



def lerAqruivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao tentar abrir o arquivo!')
    else:
        print('=' * 45)
        print('PESSOAS CADASTRADAS'.center(50))
        print('=' * 45)
        print(a.readlines())