salario = float(input('qual e o valor do seu salario?'))
if salario > 1250.00:
    salario = salario + (salario*10/100)
else:
    salario = salario + (salario*15/100)
print(f'o seu novo salario e {salario:.2f}R$')
