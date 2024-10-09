palavra = str(input('digite uma palavra qualquer:')).strip().upper()
dividir = palavra.split( )
juntar = ''.join(dividir)
print(dividir)
print(juntar)
# inverso = ''
inverso = juntar[::-1]
print(inverso)
# for x in range(len(juntar)-1,-1,-1):
#     print(juntar[x])
#     inverso += juntar[x]
# print(juntar,inverso)
# if juntar == x:
#     print(f'o nome e palindromo')
# else:
#     print(f'a Frase nao e palindromo')

