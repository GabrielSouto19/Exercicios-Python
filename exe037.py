numero = int(input('digite um numero inteiro qualquer:'))
base = str(input('qual sera a base de conversao:\n 1-Binario \n 2- Octal \n 3- hexadecimal'))
resto = 0
if base == 'Binario' or base == '1':
    print(f'{numero} convertido para binario é = {bin(numero)[2:]}')
elif base == '2':
    print(f'{numero} na base octal fica {oct(numero)[2:]}')
elif base == '3':
    print(f'{numero} na base hexadecimal e igual a {hex(numerok)[2:]}')
