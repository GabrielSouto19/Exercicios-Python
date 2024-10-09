nome = ''
preco = 0.0
tot = 0
mdemil = 0
barato = 0
nomebarato = ''
cont = 0
while True:
    nome = str(input('Digite o nome do produto:'))
    preco = float(input('Digite o preco do produto:'))
    cont += 1
    tot += preco
    if cont == 1 or preco < barato:
        barato = preco
        nomebarato = nome
    if preco > 1000.0:
        mdemil +=1
    perg = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if perg == 'N':
        break
print(f'O total gasto na compra foi de {tot:.2f}R$\n{mdemil} produtos custam mais de mil reais\nO nome do produto mais barato é {nomebarato} custando {barato:.2f}R$' )