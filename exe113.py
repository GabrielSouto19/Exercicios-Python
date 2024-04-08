def leiaint(n):

    while True:
        try:
            x = int(input(n))
        except(ValueError,TypeError):
            print('Error , tente inserir um numero inteiro valido')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mPrograma finalizado pelo usuario!\033[m')
        else:
            print(f'dado validado com sucesso! retorno de {x}')
            return x
            break


numero = leiaint('Digite um valor do tipo inteiro ')


def leiafloat(x):
    while True:
        try:
            x = float(input('Digite um numero'))
        except(ValueError,TypeError):
            print('Erro!Insira um numero do tipo float')
        else:
            print('Dado validado com sucesso Muito obrigado!')
            break


numerofloat = leiafloat('Digite um valor em float')



