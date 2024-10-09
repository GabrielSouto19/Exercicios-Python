from time import sleep
from random import randint
temp = []
perm = []
print('JOGO DA MEGA SENA')
jogos = int(input('Quantos jogos voce quer sortear:'))
for i in range(1,jogos+1):
    for x in range(1,7):
        numero = randint(1,60)
        if numero not in temp:#verifica se o numero sorteado ja nao foi escolhido anteriormente
            temp.append(numero)
    perm.append(temp[:])
    temp.clear()
for y,n in enumerate(perm):
    print(f'jogo {y+1} : {n}')
    sleep(2)

