def fatorial(n,show=False):
    f = 1
    for c in range(n,0,-1):
        if show == True:
            print(c,end='')
            if c > 1:
                print('x',end='')
            else:
                print('=',end='')
                print(f'{f}')

        f *= c
    return f
numero = int(input('Digite um numero para calculo de fatorial:'))
print(f'O fatorial de {numero} é igual a {fatorial(numero,True)}')
# help(fatorial)