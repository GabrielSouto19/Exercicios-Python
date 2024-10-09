# pares = []
# impares = []
# lista = [pares,impares]
# for i in range(1,8):
#     numero = int(input('Digite um numero:'))
#     if numero % 2 == 0:
#         pares.append(numero)
#     else:
#         impares.append(numero)
# lista[0].sort()
# lista[1].sort()
# print(f'a lista totol de numeros da lista  e igual a {(lista)}')
# print(f'a lista total de numeros pares e igual a {(lista[0])}')
# print(f'a lista total de numeros impares e igual a {(lista[1])}')

# metodo usado pelo guanabara
num = [[],[]]
valor = 0
for i in range(1,8):
    valor = int(input(f'Digite o {i}o. valor:'))
    if i % 2 == 0:
        num[0].append(i)
    else:
        num[1].append(i)
print(f'todos os numeros sao {num}')
print(f'os valores pares digitados foram {num[0]}')
print(f'os valores impares digitados foram {num[1]}')