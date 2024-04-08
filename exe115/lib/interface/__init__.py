def leiaint(x):
    while True:
        try:
            n = int(input(x))
        except(ValueError,TypeError):
            print('\033[31mPor favor , Digite um numero inteiro valido!\033[m')
        except(KeyboardInterrupt):
            print('\033[31mO usuario prefiriu não digitar nenhum numero \033[m')
            break
        else:
            return n

def linha(msg=42):
    return '-'*msg


def cabecalho(x):
    print(linha())
    print(x.center(42))
    print(linha())

def menu(lista):
    cabecalho('Menu principal')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m-\033[34m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Sua opção:')
    return opc