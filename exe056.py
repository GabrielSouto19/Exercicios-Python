lista = []
maisvelho = 0
maisvelhonome = ''
muienova = 0
mediaidade = []
mediatodos = 0
for x in range(1,5):
        print(f'{'='*20} {x} pessoa {'='*20}')
        nome = str(input('qual e o seu nome:')).title().strip()
        idade = int(input('qual e a sua idade:'))
        sexo = str(input('qual e o seu sexo [M/F]')).upper()
        lista.append([nome,idade,sexo])
        if idade > maisvelho and sexo == 'M':#if sexo in 'Mm': tambem funciona(mais aplicavel)
            maisvelho = idade
            maisvelhonome = nome
            mediaidade.append(idade)
            mediatodos +=idade
            print(f'voce e o mais velho ate agora {nome}')
        if sexo == 'F' and idade < 20:
            muienova +=1
            mediatodos += idade
            mediaidade.append(idade)
        elif sexo == 'F':
            mediaidade.append(idade)
            mediatodos += idade
print(f'a media de idade do grupo é {(mediatodos)/len(mediaidade)} anos de idade!')
print(f'o homem mais velho foi {maisvelhonome}')
print(f'mulheres com menos de 20 anos , ha {muienova} apenas!')
# print(f'a media de idade dos integrantes é{mediaidade/(len(mediaidade))}')
print(f'{mediaidade}')
print(f'{len(mediaidade)}')
# mediaidade[0] + mediaidade[]


