from time import sleep
def contador(i,f,s):#i de inicio f de final e s de salto
    if i > f:
        s = -s
        sleep(0.5)
    if s == 0 and i < f:
        s = 1
        sleep(0.5)
    else:
        s = -1
        sleep(0.5)
    for i in range(i,f,s):
        print(i,end='...')

inicio = int(input('Digite o valor de inicio:'))
final = int(input('Digite o valor de parada :'))
salto = int(input('Digite o salto:'))
contador(inicio,final,salto)

