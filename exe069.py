idade = 0
sexo = ''
maior= 0
homens = 0
muienova = 0
while True:
    sexo = str(input('sexo: [M/F]')).upper().strip()[0]
    while sexo not in 'MF':
        print('Digite uma alternativa valida!')
        sexo = str(input('sexo: [M/F]')).upper().strip()[0]

    idade = int(input('qual e a sua idade?'))
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        muienova += 1
    if idade > 18:
        maior += 1
    resp = str(input('Voce deseja continuar ? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break

print('Programa finalizado!')
print(f'O numero de homens contabilizados pelo programa foi de {homens}\nO numero de mulheres com menos de 20 anos foi de {muienova} \nO numero total de pessoas maiores de 18 anos foi de {maior} ')

