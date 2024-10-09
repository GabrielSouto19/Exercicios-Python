# le nome idade e sexo de varias pessoas
dados = {}
lista = []
soma = media = 0
mulheres = []
acimamedia = []
while True:
    dados['nome'] = str(input('Digite seu nome:'))
    dados['sexo'] = str(input('Digite seu sexo [M/F]:')).upper().strip()[0]
    while dados['sexo'] not in 'MF':
        print('Digite um valor valido')
        dados['sexo'] = str(input('Digite seu sexo [M/F]:')).upper().strip()[0]
    dados['idade'] = int(input('Digite sua idade:'))
    soma += dados['idade']
    lista.append(dados.copy())
    if dados['sexo'] == 'F':
        mulheres.append(dados.copy())
    media = soma / len(lista)
    if dados['idade'] > media:
        acimamedia.append(dados.copy())
    perg = str(input('Voce deseja continuar? [S/N]')).upper().strip()[0]
    while perg not in 'SN':
        print('Por favor digite um comando valido')
        perg = str(input('Voce deseja continuar? [S/N]')).upper().strip()[0]
    if perg == 'N':
        break

print(f'foram cadastradas {len(lista)} pessoas')
print(f'a media de idade do grupo é de {media}')
print(f'A lista com todas as mulheres digitadas e de {mulheres}')
print(f'a lista de pessoas com idade acima da media é {acimamedia}')

