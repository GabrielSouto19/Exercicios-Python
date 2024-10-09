lista = []
cont = 0
for i in range(0,5):
    valor = int(input('Digite um valor:'))
    cont += 1
    if cont == 1:
        print('Este e o primeiro valor da lista')
        lista.insert(0,valor)
    if cont > 1 and valor > max(lista):
        lista.append(valor)
        print(f'valor adicionado ao final da lista')
    if valor < min(lista):
        lista.insert(0,valor)
    if valor > min(lista) and valor < max(lista):
        if valor < lista[1]:
            lista.insert(1,valor)
        if valor < lista[2] and valor > lista[1]:
            lista.insert(2,valor)
        if valor > lista[2] and valor < lista[3]:
            lista.insert(3,valor)
print(f'a lista digitada foi {lista}')