# from math import pow,sqrt
# catop = float(input('qual a medida do cateto oposto?'))
# # ctrl + (botao de interrogaçao ) transforma a linha toda em comentario
# catad = float(input('qual e a medida do cateto adjacente?'))
# hip = (pow(catop,2))+ (pow(catad,2))
# print(f'a hipotenusa deste triangulo retangulo e {sqrt(hip)}')

from math import hypot
catop = float(input('qual o comprimento do cateto oposto?'))
catad = float(input('qual o comprimento do cateto adjacente?'))
hip = hypot(catop,catad)
print(f'o comprimento da hipotenusa é {hip}')
