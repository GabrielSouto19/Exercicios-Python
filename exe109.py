from moedas import *
preco = int(input('Digite o preco '))
perc = int(input('Digite o valor percentual: '))
print(f'A metade de {moeda(preco)}R$ e igual a {metade(preco,True)}')
print(f'O dobro de {moeda(preco)} e igual a {dobro(preco,True)}')
print(f'Aumentando {perc}% sobre o valor de {moeda(preco)} temos um total de {aumentar(preco,perc,True)}')
print(f'descontando {perc}% sobre o valor de {moeda(preco)} temos um montante total de {diminuir(preco,perc,True)}')