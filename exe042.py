a = int(input('qual e o valor do lado a do triangulo'))
b = int(input('qual e o valor do lado b do triangulo'))
c = int(input('qual e o valor do lado c do triangulo'))
if a < b + c and a > b - c:
    print('o lado A pode ser considerado um lado do triangulo')
else:
    print('o lado A  nao pode ser considerado um lado do triangulo ')

if b < a + c and b > a - c:
    print('o lado B pode ser considerado um lado do triangulo')
else:
    print('o lado B  nao pode ser considerado um lado do triangulo ')

if c < a + b and b > a - b:
    print('o lado C pode ser considerado um lado do triangulo')
else:
    print('o lado C nao pode ser considerado um lado do triangulo ')

if (a < b + c and a > b - c) and (b < a + c and b > a - c) and (c < a + b and b > a - b):
    print('O triangulo condiz as condiçoes de existencia , portanto podera existir')
if a != b and a != c:
    print('Este triangulo e \033[34m Escaleno\033[34m!')
elif a == b or a == c or c == b:
    print('Este triangulo é \033[34m Isóceles \033[34m!')
elif a == c and a == b:
    print('Este triangulo é  \033[34m Equilatero \033[34m!')

