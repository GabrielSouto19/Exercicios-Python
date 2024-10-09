peso = float(input('digite  seu peso em KG:'))
alt = float(input('digite sua altura em M:'))
imc = peso /(alt**2)
print(f' o seu imc e igual a \033[34m{imc:.2f}\033[m')
if imc < 18.5:
    print('toma cuidado esta abaixo do peso')
elif imc >= 18.5 and imc <= 25.0:
    print('Voce esta no peso ideal!')
elif imc > 25.0 and imc <= 30.0:
    print('Voce esta com sobrepeso!')
elif imc > 30 and imc <= 40.0:
    print('O gordao para de comer pao de queijo ta obeso ja')
elif imc > 40.0:
    print('nuu mermao cuidado pra nao pisar na teta , obeso morbido')



