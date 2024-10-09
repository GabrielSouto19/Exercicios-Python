# numero = int(input('Digite um numero qualquer:'))
# fatorial = numero = cont
# ant = cont - 1
# while cont > 1:
#     print(fatorial)
#     print(numero)
#     fatorial = cont * ant
#     print(f'{numero}!={fatorial}')
#     cont = cont - 1

# numero = int(input('digite um numero'))
# cont = numero -1
# fat = numero
# while cont > 1:
#     print(cont)
#     fat = fat * cont
#     cont = cont -1
#     print(f'fatorial {fat}')
# print(fat)
#
# numero = int(input('digite um numero'))
# cont = numero -1
# fat = numero
# print(numero,'x ',end='')
# while cont > 0:
#     # print(numero,end='')
#     print(cont,'x ',end='')
#     fat = fat * cont
#     cont = cont -1
# print(f' = {fat}')

# tentando fazer com for
# numero = int(input('Digite um numero qualquer'))
# fat = numero
# for c in range(numero-1,1,-1):
#     fat *= c
#     print(f'{numero}x{c}')
# print(f'{numero}! = {fat}')
# # usando modulo math para resolver
# from math import factorial
# n = int(input('escolha qualquer numero inteiro:'))
# fac = factorial(n)
# print(f'o fatorial de {n} e igual a {fac}')


numero = int(input('escolha qualquer numero inteiro'))
c = numero
f = 1
while c > 0:
    f *= c
    print(f'{c}',end='')
    print('x' if c > 1 else '=',end='')
    c -= 1

print(f)

