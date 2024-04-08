# import random
# repetir = range(1,5)
# sorteio = random.choice(repetir)
# numero = int(input('advinhe qual é o numero de 1 a 5:'))
# if sorteio == numero:
#     print('acertou mizeraviii')
# else:
#
#     print('errroooou')

from random import randint
from time import sleep
computador = randint(0,5)#sorteia um numero
jogador = int(input('escolha um numero'))
print('Processando...')
sleep(3)#espera x segundos
if computador == jogador:
    print('parabens voce acertou')
else:
    print('erroooooou')
