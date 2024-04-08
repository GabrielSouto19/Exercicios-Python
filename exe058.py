from random import randint
sorteio = randint(0,11)
tent = 1
numero = 0
while numero != sorteio:
    numero = int(input('tente advinhar qual e o numero que estou pensando!!!'))
    if numero != sorteio and numero < sorteio:
        print('Errou cria!!! ')
        print('um pouco mais cria')
    elif numero!= sorteio and numero > sorteio:
        print('um pouco menos cria')
    tent += 1
print(f'acertou mizeravi , precisou de {tent} tentativas pra tu acertar')
