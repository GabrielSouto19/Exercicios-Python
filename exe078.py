lista = []
for i in range(0,5):
    lista.append(int(input('Digite um valor:')))
print(f'o maior valor digitado foi {max(lista)}\nO menor valor digitado foi {min(lista)}')
# print(f'A posicao do maior valor digitado foi {lista.index(max(lista))}')
# print(f'A posicao do menor valor digitado foi {lista.index(min(lista))}')
ultimaposicaoma = lista.index(max(lista))
ultimaposicaome = lista.index(min(lista))
print(f'o maior valor aparece {lista.count(max(lista))} vezes na lista nas posicoes',end='')
for i in range(0,lista.count(max(lista))):#laco vai de 1 ate o numero de vezes que o maior valor aparece na lista
    print(f' {lista.index(max(lista),ultimaposicaoma)}, ',end='')
    ultimaposicaoma += 1
print(f'o menor valor aparece {lista.count(min(lista))} vezes na lista nas posicoes ',end='')
for x in range(0,lista.count(min(lista))):
    print(f'{lista.index(min(lista),ultimaposicaome)},',end='')
    ultimaposicaome += 1