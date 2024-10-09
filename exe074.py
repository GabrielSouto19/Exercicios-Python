from random import randint
numero = ()
menor = maior = cont = 0
for i in range(0,5):
    aleatorio = randint(0,10)
    numero += (aleatorio,)
    cont += 1
    if cont == 1 or aleatorio < menor:
        menor = aleatorio
    if aleatorio > maior:
        maior = aleatorio
print(f'a listagem dos total de numeros sorteados e {numero} o maior valor é {maior} e o menor valor e {menor}')
# metodo alternativo usando max()
print(f'o maior valor foi {max(numero)} e o menor valor sorteado foi {min(numero)}')