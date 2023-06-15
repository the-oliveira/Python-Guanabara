import urllib
import urllib.request
#Utilizando uma biblioteca para verificar se o pc consegue acessar o site alvo.
try:
    site = urllib.request.urlopen('https://www.youtube.com')
except urllib.error.URLError:
    #Erro gerado caso o comando não acesse o site por algum motivo.
    print('Não consegui acessar o site!!')
else:
    print('Consegui acessar o site!!')