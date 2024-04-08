
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



