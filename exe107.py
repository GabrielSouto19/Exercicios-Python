import moedas

numero = int(input('Digite um numero:'))
porc = int(input('Qual e a % que vamos trabalhar:'))
print(f'O  valor de {numero} com um aumento de {porc}% fica {moedas.aumentar(numero,porc)}')
print(f'O dobro de {numero} e igual a {moedas.dobro(numero)}')
print(f'A metade de {numero} e igual a {moedas.metade(numero)}')
print(f'O valor de {numero} com um desconto de {porc}% e igual a {moedas.diminuir(numero,porc)}')