listatemp =[]
listafi = []
cont = 0
while True:
    nome = str(input('Digite o nome do aluno:')).strip().title()
    nota1 = float(input('Digite a primeira nota do aluno:'))
    nota2 = float(input('Digite a segunda nota do aluno:'))
    listatemp.append(nome)
    listatemp.append(nota1)
    listatemp.append(nota2)
    listafi.append(listatemp[:])
    listatemp.clear()
    cont += 1
    perg = str(input('Voce quer continuar? [S/N]')).upper().strip()[0]
    while perg not in 'SN':
        perg = str(input('Voce quer continuar? [S/N]')).upper().strip()[0]#validaçao de dados
    if perg == 'N':
        break
print('=-'*50)
print(f'{"No":<10} {"Nome":^10}{"media":>10}')
for i,n in enumerate(listafi):
    print(f'{i:<10}{n[0]:^10}{((n[1] + n[2]) / 2):>10.2f}')
n = int(input('Ver notas de qual aluno:(999 para interromper)'))
for nota in listafi:
    if n > len(listafi):
        print(f'Digite um valor valido')
        n = int(input('Ver notas de qual aluno:(999 para interromper)'))
    print(f'notas de {nota[0]}:[{nota[1]}] e [{nota[2]}]')
    n = int(input('Ver notas de qual aluno:(999 para interromper)'))


