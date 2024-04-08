from time import sleep
jogador = {}
gols = []
totgol = qgol = cont = 0
lista = []
while True:
    jogador['nome'] = str(input('Digite o nome do jogador:')).title()
    jogador['partidas'] = int(input('Quantas partidas ele jogou?'))
    for i in range(0,jogador['partidas']):
        qgol = int(input(f'Quantos gols ele fez na {i}a partida?'))
        gols.append(qgol)
        totgol += qgol
    jogador['gols'] = gols[:]
    jogador['total de gols'] = totgol
    gols.clear()
    totgol = 0
    lista.append(jogador.copy())
    perg = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if perg == 'N':
        break
print(f'A lista completa e {lista}')
for x in lista:
    print(f'{x['nome']} fez um total de {x['total de gols']}')
print('=-'*30)
print(f'{"cod":<0}{"nome":^15}{"gols":^20}{"TOTAL":^40}')
print("-"*60)
for x,n in enumerate(lista):
    print(f'{x:< 0}{n['nome']:^15}{n['gols']}{n['total de gols']:^40}')
n = 0
#jeito do guanabara :
# for i,x in enumerate(lista):
#     print(f'{i}:>3',end=' ')
#     for y in x.values():
#         print(f'{y:>5}',end='')


while True:
    print('-'*60)
    mostrar = int(input('Mostrar dados de qual jogador?(999 para encerrar)'))
    while mostrar < len(lista):
        print('Digite um valor valido!')
    if mostrar == 999:
        print('FINALIZANDO',end='')
        sleep(0.5)
        print('.',end='')
        sleep(0.5)
        print('.',end='')
        sleep(0.5)
        print('.',end='')
        sleep(0.5)
        print('.',end='')
        break
    for c,v in lista[mostrar].items():
        if c == 'nome':
            print(f'levantamento do jogador {v}')
        if c == 'gols':
            for g,e in enumerate(v):
                print(f'No jogo {g} fez {e} gols!')

