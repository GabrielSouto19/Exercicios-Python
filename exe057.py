# sexo = 'M'
# while sexo in 'MF':
#     sexo = str(input('Digite seu sexo [M/F]')).upper().strip()
#     if sexo == 'M':
#         print('voce e macho')
#     elif sexo == 'F':
#         print('voce e femea')
#     else:
#         print(f'nao aceitamos nao binario aqui')

sexo = 'M'
sexo = str(input('Digite seu sexo [M/F]')).upper().strip()[0]#considera somente a primeira letra
if sexo in 'MF':
    print(f'voce e {sexo}')
else:
    while sexo !='M' or sexo != 'F':
        print(f'nao aceitamos nao binario aqui!')
        sexo = str(input('Digite seu sexo [M/F]')).upper().strip()
