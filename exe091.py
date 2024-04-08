from random import randint
# real = []
# temp = {}
# nomemaior = []
# maior = cont = 0
# for i in range(1,5):
#     temp['nome'] = str(input('Digite seu nome:')).title()
#     temp['dado'] = randint(1,6)
#     if temp['dado'] >= maior:
#         maior = temp['dado']
#         nomemaior.clear()
#         nomemaior.append(temp['nome')
#     real.append(temp.copy())
#     temp.clear()
#     cont += 1
# for x in real:
#     print(f'{x['nome']} tirou {x['dado']}')
#
# print(f'nome dos ganhadores:')
# for y in nomemaior:
#     print(f'{y} ',end='')
#
# pessoa = {}
# temp = []
# numeros = []
# from random import randint
# for i in range (1,5):
#     pessoa['nome'] = str(input('Digite o nome:'))
#     pessoa['dado'] = randint(1,6)
#     temp.append(pessoa.copy())
#     numeros.append(pessoa['dado'])
# print(temp)
# numeros.sort(reverse=True)
# print(numeros)
# print(max(numeros))
# resoluçao do guanabara
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1':randint(1,6),
    'jogador2':randint(1,6),
    'jogador3':randint(1,6),
    'jogador4':randint(1,6)
}
ranking = {}#tratar como lista
print('Valores Sorteados :')
for c,v in jogo.items():
    print(f'{c} tirou {v}')
    sleep(1)
print('=-'*30)
print('RANKING')
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)#itemgetter 1 ordena pela valor e 0 pela chave
for x,y in enumerate(ranking):
    print(f'{x+1}-{y[0]} com {y[1]}')