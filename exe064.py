valor = soma = numero = 0
while valor != 999:
    valor = int(input('Digite outro valor'))
    if valor != 999:
        soma += valor
        numero +=1
print(f'programa finalizado a soma dos numeros digitados sao {soma}! , voce digitou {numero} numeros!')
