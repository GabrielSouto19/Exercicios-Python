from pythonProject1exercicios.exe115.lib.interface import *
def arquivoexiste(nome):
    try:
        a = open(nome,'rt')#funcao open tenta abrir um arquivo , parametro rt e para leitura do arquivo
        a.close()
    except FileNotFoundError:#se o arquivo não foi encontrado
        return False
    else:
        return True
def criararquivo(nome):
    try:
        a = open(nome,'wt+')#wt escreve um arquivo de texto o + e para se o arquivo nao existir ele cria
        a.close()
    except:
        print('Houve um erro  na criação do arquivo!')
    else:
        print(f'Arquivo de texto {nome} criado com sucesso!')


def lerarquivo(nome):
    try:
       a = open(nome,'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print('Arquivo lido com sucesso')
        cabecalho('Pessoas Cadastradas:')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace(';','')
            print(f'{dado[0]} e igual a {dado[1]}avnos ')
    finally:
        a.close()


def cadastrar(arq,nome='Desconhecido',idade=0):
    try:
        a = open(arq,'at')
    except:
        print('Algo deu errado na execução do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} de {idade} anos!')
            a.close()



