# import random
# n1 = input('primeiro aluno')
# n2 = input('segundo aluno')
# n3 = input('terceiro aluno ')
# n4 = input('quarto aluno')
# lista = [n1,n2,n3,n4]
# sorteio = random.choice(lista)
# print(f'o candidato sorteado foi {sorteio}')

from random import choice
n1 = input('primeiro aluno')
n2 = input('segundo aluno')
n3 = input('terceiro aluno ')
n4 = input('quarto aluno')
lista = [n1,n2,n3,n4]
sorteio = choice(lista)
print(f'o candidato sorteado foi {sorteio}')
# quando se importa um comando especifico pode se tirar a referncia a biblioteca
# random.choice somente se importar toda a biblioteca
# caso importar choice espicifico pode se colocar apenas o comando choice
