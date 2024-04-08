import moeda#solucao do guanabara exe109
p = float(input('Digite um valor:'))
print(f'O dobro de {moeda.moeda(p)} e igual a {moeda.dobro(p,True)}')
print(f'A metade de {moeda.moeda(p)} e igula a {moeda.metade(p,True)}')
print(f'O valor de {moeda.moeda(p)} com um acrescimo de 10% e igual a {moeda.aumentar(p,10,True)}')
print(f'O valor de {moeda.moeda(p)} com um desconto de 15% e igual a {moeda.diminuir(p,15,True)}')
