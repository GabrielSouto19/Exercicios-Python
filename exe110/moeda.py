
def aumentar(preco=0,taxa=0,formt=False):
    res = preco + (preco*taxa/100)
    return res if formt == False else moeda(res)


def metade(preco=0,formt=False):
    res = preco/2
    return res if formt == False else moeda(res)


def dobro(preco=0,formt=False):
    res = preco * 2
    return res if formt == False else moeda(res)


def diminuir(preco=0,taxa=0,formt=False):
    res = preco - (preco*taxa/100)
    return res if formt == False else moeda(res)

def moeda(p=0,moeda='R$'):
    return f'{moeda}{p:.2f} '.replace('.',',')#substitui o ponto pela virgula

def resumo(p=0,taxaa=0,taxad=0,):
    print('=-'*15)
    print('RESUMO DO VALOR'.center(30))#forma alternativa de centralizar uma string .center
    print('=-'*15)
    print(f'Preço analisado:\t{moeda(p)}')
    print(f'O dobro do preco:\t{dobro(p,True)}')#para mostrar uma tabulaçao apertaoms \t
    print(f'A metade do preco:\t{metade(p,True)}')
    print(f'{taxaa}% de aumento:\t \t{aumentar(p,taxaa,True)}')
    print(f'{taxad}% de desconto:\t \t{diminuir(p,taxad,True)}')
    print('=-'*15)

