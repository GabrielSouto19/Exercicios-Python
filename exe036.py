casa = float(input('qual e o valor da casa?'))
sal  = float(input('qual e o valor do seu salario?'))
temp = int(input('em quantos anos voce pretende pagar:'))
parcela = casa/(temp *12)
if parcela > (sal*30/100):
    print('imprestimo negado')
else:
    print('boa sorte com a casa nova ')