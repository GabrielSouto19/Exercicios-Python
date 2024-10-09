jogador = {}
gols = []
totgol = qgol = 0
jogador['nome'] = str(input('Digite o nome do jogador:'))
jogador['partidas'] = int(input('Digite o numero de partidas jogadas:'))
for i in range(1,jogador['partidas']+1):
    qgol = int(input(f'quantos gols o jogador fez {i}a partida?'))
    gols.append(qgol)
    totgol += qgol
jogador['gols'] = gols
jogador['total de gols'] = totgol
print(jogador)
for x,y in jogador.items():
    print(f'{x}:{y}')#nome :gabriel
    if x == 'partidas':#partida
        for a in range(0,y):
            print(f'Na {a+1}a partida ele fez {jogador['gols'][a]}')
print(sum(gols))#soma os numeros contidos na lista
