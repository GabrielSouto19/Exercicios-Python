lista = []
while True:
    numero = int(input('Digite um numero'))
    if numero not in lista:
        lista.append(numero)
    else:
        print('Este numero ja foi digitado')
    perg = str(input('Que continuar ?[S/N]')).strip().upper()[0]
    if perg == 'N':
        break
print(f'A lista digitada foi {lista}')
lista.sort()
print(f'a lista ordenada e {lista}')
lista.sort(reverse=True)
print(f'a lista ordenada reversamente e {lista}')