from datetime import datetime
rg = {}
lista = []
rg['nome'] = str(input('Digite o seu nome:'))
rg['idade'] = datetime.now().year - int(input('Digite o ano de nascimento'))
rg['CTPS'] = int(input('ctps:(0 se nao tem )'))
if rg['CTPS'] != 0:
    rg['Contratação'] = int(input('Digite o ano de contrataçao'))
    rg['salario'] = float(input('Digite o seu salario:'))
    rg['aposentadoria'] = datetime.now().year - rg['Contratação'] + 35 + rg['idade']#35 anos devido ao periodo de contribuiçao pela lei vijente ate 2024
lista.append(rg.copy())
print(f'{lista}')
for i in lista:
    for x,y in i.items():
        print(f'{x} tem valor {y}')

