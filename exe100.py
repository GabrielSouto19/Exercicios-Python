numeros = []
from random import randint
def sorteia(lista):
    for i in range(1,6):
        lista.append(randint(1,10))


def somapar(listasoma):
    aux = 0
    for i in listasoma:
        if i % 2 == 0:
            aux += i
    print(f'A soma dos valores pares encontrados foi {aux}')


print('SORTEANDO O NUMERO:')
sorteia(numeros)
print(f'numeros sorteados!{numeros}')
print('SOMANDO OS PARES!')
somapar(numeros)





