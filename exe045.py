from random import choice
escolha = int(input('escolha:\n1-pedra\n2-papel\n3-tesoura\n'))
jokenpo = ['Pedra' , 'Papel' , 'Tesoura']
sorteio = choice(jokenpo)
print(sorteio)
if escolha == 1 and sorteio == 'Papel':
    print('hahaha eu venci!')
elif escolha == 1 and sorteio == 'Pedra':
    print('empate!!!')
elif escolha == 1 and  sorteio == 'Tesoura':
    print('voce ganhou')

if escolha == 2 and sorteio == 'Papel':
    print('empate!!!')
elif escolha == 2 and sorteio == 'Pedra':
    print('voce ganhou!!!')
elif escolha == 2 and  sorteio == 'Tesoura':
    print('eu ganhei')

if escolha == 3 and sorteio == 'Papel':
    print('hahaha eu venci!')
elif escolha == 3 and sorteio == 'Pedra':
    print('voce ganhou!!!')
elif escolha == 3 and  sorteio == 'Tesoura':
    print('empate')



