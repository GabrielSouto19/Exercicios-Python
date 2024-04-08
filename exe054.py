from datetime import date
ano = int(input('qual e o ano de seu nascimento'))
idade
maioridade = 0
for x in range(1,7):
    idade = int(input('qual e a sua idade:'))
    if idade >= 21:
        maioridade +=1
        print('Voce ja e maior de idade!')
print(f'o total foi de {maioridade} pessoas com maioridade alcancada')

