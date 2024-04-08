from random import randint

print('''-------------------------
Vamos jogar par ou impar
----------------------------''')
vitcon = 0
while True:
    sorteio = randint(0,10)
    esc = int(input('escolha um numero'))
    pi= str(input('escolha par ou impar[P/I]')).upper().strip()[0]
    print(f'Eu escolhi {sorteio}')
    resul = esc + sorteio
    if resul % 2 == 0:
        print(f' e par')
        if pi == 'P':
            print('voce ganhou parabens !')
            vitcon+=1
        elif pi == 'I':
            print('Eu ganhei otario')
            break
    elif resul % 2 != 0 :
        print(f'e impar')
        if pi == 'I':
            print(f' voce ganhou!!!.')
            vitcon +=1
        elif pi == 'P':
            print('eu ganhei hehehe')
print(f'o total de vitorias seguidas foi de {vitcon}')




