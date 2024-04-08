velocidade = float(input('qual e a velocidade do carro em km/h:'))
limite = 80.0
if velocidade >= limite:
    print('levou multa chefe')
    print(f'o valor da multa sera de {(velocidade-limite)*7.00:.2f}R$')
else:
    print('vai tranquilo')