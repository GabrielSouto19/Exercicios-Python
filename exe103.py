# def ficha(nome='Desconhecido',gols=0):
#     return f'O Jogador {nome} fez {gols} gol(s).'
#
#
# cria = str(input('Digite seu nome de cria:')).title()
# gol = str(input('Digite quantos gols Voce fez'))
# if cria == '' and gol == '':
#     print(ficha())
# elif cria == '' :
#     print(ficha(gols=gol))
# elif gol == '':
#     print(ficha(cria))
# else:
#     print(ficha(cria,gol))
#
# solucao do guanabara ,exercicio resolvido
def ficha(nome='<Desconhecido>',gols=0):
    print(f'O jogador {nome} fez um total de {gols} gol(s).')


n = str(input('Digite o nome do Jogador:')).title()
g = str(input('Número de gols:'))
if g.isnumeric():#verifica se o texto pode ser convertido em numero quase uma validaçao de dado
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha()
else:
    ficha(n,g)