numeros = []
tot = 0
while True:
    numeros.append(int(input('Digite um numero:')))
    tot += 1
    perg = str(input('Voce quer continuar? [S/N]')).strip().upper()[0]
    if perg == 'N':
        break
print(f'o total de numeros digitados foi de {tot} numeros')
numeros.sort(reverse=True)
print(f'a lista ordenada de maneira decrescente esta representada a seguir:{numeros}')
if 5 in numeros:
    print(f'o valor 5 foi digitado e esta na lista')
else:
    print(f'o valor 5 nao foi digitado!')