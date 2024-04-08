numero = soma = quant = 0
while True:
    numero = int(input('escolha um numero:(digite 999 para parar)'))
    if numero == 999:
        break
    soma += numero
    quant += 1
print(f'a soma dos numeros digitados é de {soma} e a quantidade de numeros digitados foi de {quant}')
