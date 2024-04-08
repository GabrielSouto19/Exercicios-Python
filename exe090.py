from time import sleep
aluno = {}
lista = []
while True:
    aluno['nome'] = str(input('Digite o nome do aluno:'))
    aluno['media'] = float(input('Digite qual foi a media do aluno'))
    aluno['situacao']= 'APROVADO' if aluno['media'] > 6.0 else 'REPROVADO'
    lista.append(aluno.copy())
    perg = str(input('Voce quer continuar?[S/N]')).upper().strip()[0]
    if perg == 'N':
        print('Finalizando',end='')
        sleep(0.5)
        print('.',end='')
        sleep(0.5)
        print('.',end='')
        sleep(0.5)
        print('.',end='')
        sleep(0.5)
        print()
        break
for c,v in aluno.items():
    print(f'{c}:{v}')
