# solucao do guanabara
matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = soma3col = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para: [{l}], [{c}]'))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
print(f'{'=-'*70}')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')

    print()
print(f'a soma dos valores pares e igual a {par}')
print(f'o maior valor da segunda linha e igual a {max(matriz[1])}')
for l in range(0, 3):
    soma3col += matriz[l][2]
print(f'a soma dos valores da 3o coluna e igual a {soma3col}')
