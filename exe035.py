reta1 = int(input('qual e o comprimento do primeiro lado do triangulo'))
reta2 = int(input('qual e o comprimento do segundo lado do triangulo'))
reta3 = int(input('qual e o comprimento do terceiro lado do triangulo'))
diferenca = reta2 - reta3
soma = reta2 + reta3
if reta1 > diferenca and reta1 < soma:
    if diferenca < 0:
        diferenca = diferenca *(-1)

    print('o triangulo pode existir ')

else:
    print(' o triangulo nao pode existir ')


