# termo1 = int(input('qual e o primeiro termo:'))
# ordem = int(input('qual a ordem da p.a'))
# raz = int(input('digite a razao:'))
# cont = 0
# novo = ''
# while ordem != cont and termo1 != 0:
#     if termo1 != 0:
#         cont += 1
#         print(f'{termo1}')
#         termo1 += raz
#     novo = str(input('Voce deseja mostrar mais alguns termos?')).upper().strip()
#     if novo == 'S':
#         termo1 = int(input('qual e o primeiro termo:'))
#         ordem = int(input('qual a ordem da p.a'))
#         raz = int(input('digite a razao:'))
#         if termo1 == 0:
#             break
#     else:
#         print(f'{termo1}')

termo1 = int(input('qual e o primeiro termo:'))
ordem = int(input('qual a ordem da p.a'))
raz = int(input('digite a razao:'))
cont = 0
while ordem != 0:
    cont = 0
    while ordem != cont:
        if ordem != cont:
            cont += 1
            print(termo1)
            termo1 += raz
    perg = int(input('Voce deseja mostrar mais quantos termos ?'))
    ordem = perg
print('Programa finalizado!!!')

