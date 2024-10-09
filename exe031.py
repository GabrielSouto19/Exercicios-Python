viagem = float(input('qual a distancia da viagem em km ?'))
if viagem <= 200:
    print(f'o preco da viagem sera de {viagem*0.50}R$')
else:
    print(f'o preco da viagem e de {viagem*0.45}R$')