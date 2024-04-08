# # cont = int(input('Quantos numeros da sequencia vc quer analisar:'))
# # numero = 0
# # termo1 = 0
# # termo2 = 1
# # termo3 = termo1+termo2
# # while numero < cont:
# #     if numero == 1:
# #         print(termo1)
# #     elif numero == 2:
# #         print(termo1)
# #         print(termo2)
# #     numero += 1
# #     print(termo1)
# #     print(termo2)
# #     print(termo3)
# #     termo1 = termo2
# #     termo2 = termo3
# #     termo3 = termo1+ termo2
#
#
# cont = 0
# termo1 = 0
# termo2 = 1
# termo3 = termo2+termo1
# print(f'{termo1}')
# # print(f'o termo2 e {termo2}')
# while cont < 3:
#     # print(termo1)
#     print(f'{termo2}')
#     print(f'{termo3}')
#     termo1 = termo3 # termo 1 passa a ser o segundo e o segundo passa a ser o terceiro
#     termo2 = termo3
#     termo3 = termo3 + termo2
#     print(termo3)
#     # print(termo3+(termo2+termo3))
#     cont += 1
# resoluçao do exercicio
#
c=2
ordem = int(input('Qual a ordem dos termos ?'))
t1 = 0
t2 = 1
print(t1)
print(t2)
while c < ordem:
    t3 = t1 + t2
    print(t3)
    # print(t1)
    # print(t2)
    t1 = t2
    t2 = t3
    c +=1
# consegui fazer sozinho

