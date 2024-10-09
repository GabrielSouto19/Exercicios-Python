from math import sin,tan,cos,radians
angulo = float(input(f'digite o valor de um angulo'))
cose = cos(radians(angulo))
tang = tan(radians(angulo))
sen = sin(radians(angulo))
print(f'o seno deste angulo é {sen:.2f} \n o cosseno dele {cose:.2f} \n e a tangente dele e {tang:.2f}')