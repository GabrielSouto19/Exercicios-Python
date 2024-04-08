import moedas
numero = int(input('Digite um numero:'))
porc = int(input('Qual e a % que vamos trabalhar:'))
print(f'O valor do dobro de {moedas.moeda(moedas.dobro(numero))} formatado e igual a {moedas.moeda(moedas.dobro(numero))}')
