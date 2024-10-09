velocidade = float(input('Digite a velocidade registrada:'))
if velocidade > 80:
    print(f'Alerta sua velocidade registrada foi de {velocidade} Km/h . MULTA:{(velocidade-80)*4:.2f}R$')
else:
    print(f'Velocidade dentro do limite tolerave!')