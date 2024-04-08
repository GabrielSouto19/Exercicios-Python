pessoas = []
tot = []
pes = 0
totpeso = []
while True:
    pessoas.append(str(input('Digite seu nome:')).strip().title())
    pessoas.append(int(input('Digite seu peso em Kg:')))
    totpeso.append(pessoas[-1])
    tot.append(pessoas[-2:])
    pes += 1
    perg = str(input('Voce quer continuar?[S/N]')).strip().upper()[0]
    while perg not in 'SN':
        perg = str(input('Voce quer continuar?[S/N]')).strip().upper()[0]
    if perg == 'N':
        break
print(f'o total de pessoas cadastradas foi {pes}')
print(f'o maior peso foi de {max(totpeso)}Kg. de ',end=',')
for i in tot:
    if i[1] >= max(totpeso):
        print(f'{i[0]} e...',end='')
print(f'\nE o menor peso foi de {min(totpeso)}KG de ',end='')
for i in tot:
    if i[1] <= min(totpeso):
        print(f'{i[0]} e...')

