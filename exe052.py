numero = int(input('digite um numero inteiro:'))
divisores = 0
for x in range(1,numero+1):
    print(f'o numero {numero} divido por {x} e igual a {numero//x} ')
    if numero % x == 0:
        print('adicioando mais um aos divisores')
        divisores +=1
print(divisores)
if divisores > 2:
    print('Este numero nao e primo!')
else:
    print('Este numero e primo')