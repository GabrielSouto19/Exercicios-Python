numeros = []
pares = []
impares = []
perg = ''
while True:
    valor = int(input('Digite um numero:'))
    numeros.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    perg =str(input('Voce quer continuar?[S/N]')).upper().strip()[0]
    while perg not in 'SN':
        perg =str(input('Voce quer continuar?[S/N]')).upper().strip()[0]
    if perg == 'N':
        break
print(f'lista geral:{numeros}\nNumeros pares{pares}\nNumeros impares {impares}')
# solucao alternativa do guanabara
# colocar um for no final do programa percorrendo a lista
# for i , v in enumerate(numeros):
#     if i % 2 == 0:
#         pares.append(i)
#     else:
#         impares.append(i)

