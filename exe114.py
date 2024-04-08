import urllib # biblioteca para requisicoes no protocolo http
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br')#tenta abrir a url
# except:
#     print('Algo deu errado tente novamente mais tarde !')
except(urllib.error.URLError):
    print('O site  pudim nao esta disponivel')

else:
    print('Consegui acessar o site  ')

# conseguimos pegar o conteudo html que esta no site colocando o print(site.read())
