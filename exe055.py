maiorpe = 0.0
menorpe = 12200.0
for x in range(1,6):
    peso = float(input('qual e o seu peso:'))
    if peso > maiorpe:
        maiorpe = peso
        print(f'o peso de {maiorpe}foi o maior ate agora!')
    elif peso < menorpe:
        menorpe = peso
        print(f'este foi o menor peso ate agora')

print(f'o maior peso contabilizado foi{maiorpe}KG e o menor foi{menorpe}KG')