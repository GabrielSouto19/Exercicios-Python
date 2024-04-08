perg = ''
lista = []
media = 0
numeros = 0
maior = 0
menor = 31332323

while perg != 'N':
    valor = int(input('Digite um numero!'))
    media += valor
    numeros +=1
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    perg = str(input('Voce quer continuar[S/N]?')).upper().strip()[0]
    if perg not in 'SN':
        print('por favor digite uma resposta valida')
print(f'a media dos numeros digitados foi{media/numeros:.2f} o maior valor foi {maior} e o menor valor foi {menor}')

