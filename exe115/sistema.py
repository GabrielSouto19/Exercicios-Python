from lib.interface import *
from time import sleep
from lib.arquivo import *
arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    resp = menu(['Ver pessoas cadastradas','Cadastrar Nova Pessoa','Sair Do Sistema'])
    if resp == 1:
        lerarquivo(arq)
        cabecalho('Mostrando Pessoas Cadastradas!')
    elif resp == 2:
        cabecalho('Novo Cadastro!')
        nome = str(input('Digite seu nome:'))
        idade = leiaint('Digite sua idade')
        cadastrar(arq,nome,idade)
    elif resp == 3:
        cabecalho('Finalizando sistema!!!')
        break
    else:
        print('\033[31mDigite um opção valida\033[m')
    sleep(3)
