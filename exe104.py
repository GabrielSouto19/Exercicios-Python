def leiaint(numero):
    while True:
        numero = str(input('Digite um numero:'))
        if numero.isnumeric():
            numero = int(numero)
            print(f'Dado Validado com sucesso!')
            break
        else:
            print('\033[31mErro digite um dado valido! \033[m')
        perg = str(input('Voce deseja continuar?[S/N]')).upper().strip()[0]
        while perg not in 'SN':
            perg = str(input('Voce deseja continuar?[S/N]')).upper().strip()[0]
        if perg == 'N':
            break

#Programa principal
n = str
leiaint(n)
# print(f'Voce acabou de Digitar o numero {n}')
