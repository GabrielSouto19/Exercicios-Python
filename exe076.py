produtos = ()
cont = 0
sucessor = 1
for i in range(0,5):
     novopro = str(input('Qual e o nome deste produto:'))
     preco = float(input('qual o preco deste produto:'))
     produtos += (novopro,preco)

print(f'a listagem final de produtos foi {produtos}')
print(80*'=')
print(f'{'LISTAGEM DE PRECO':^80}')
print(80*'=')
for i in range(0,len(produtos)):
    if cont >= len(produtos):
        break
    print(f'{produtos[cont]}...................................{produtos[cont+1]:.2f}R$')
    cont += 2

# forma alternativa do guanabara
for x in range(0,len(produtos)):
    if x % 2 == 0:
        print(f'{produtos[x]:.<30}',end='')
    else:
        print(f'R${produtos[x]:.>5.2f}')