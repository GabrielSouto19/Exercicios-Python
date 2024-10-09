numeros = ()
par = ()
for i in range(0,5):
    aleatorio = int(input('Digite um numero:'))
    numeros += (aleatorio,)
    if aleatorio % 2 == 0:
        par += (aleatorio,)
if 3 in numeros:
    x = 'numeros.index(3)'
else:
    x = 0
print(numeros)
print(f'o valor 9 apareceu {numeros.count(9)} vezes')
print(f'o numero 3 aparece primeiramente na posicao {numeros.index(3)}'if 3 in numeros else 'o numero 3 nao foi digitado nenhuma vez')
print(f'os valores pares mostrados sao {par}')