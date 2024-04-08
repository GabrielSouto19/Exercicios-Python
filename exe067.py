numero = cont = 0
while True:
    numero = int(input('qual numero voce quer consultar a tabuada:(Digite qualquer valor negativo para finalizar o programa)'))
    if numero < 0:
        break
    for x in range(1,11):
        print(f'{numero} x {x} = {numero*x}')
print(f'O Programa foi finalizado com sucesso!')
