import moeda#solucao do guanabara
p = float(input('Digite um valor:'))
print(f'O dobro de {moeda.moeda(p)} e igual a {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} e igula a {moeda.moeda(moeda.metade(p))}')
print(f'O valor de {moeda.moeda(p)} com um acrescimo de 10% e igual a {moeda.moeda(moeda.aumentar(p,10))}')
print(f'O valor de {moeda.moeda(p)} com um desconto de 15% e igual a {moeda.moeda(moeda.diminuir(p,15))}')
