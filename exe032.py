from datetime import date #para usar a data atual da maquina
ano = int(input('em que ano estamos:'))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0) and (ano % 100 != 0) and (ano % 400 != 0):
    print(f'o ano de {ano} é bissexto!')
else:
    print('estamo em um ano normal ')
