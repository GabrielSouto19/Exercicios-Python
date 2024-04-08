import moeda
p = float(input('Digite um valor:'))
print(f'O dobro de {p} e igual a {moeda.dobro(p)}')
print(f'A metade de {p} e igula a {moeda.metade(p)}')
print(f'O valor de {p} com um acrescimo de 10% e igual a {moeda.aumentar(p,10)}')
print(f'O valor de {p} com um desconto de 15% e igual a {moeda.diminuir(p,15)}')