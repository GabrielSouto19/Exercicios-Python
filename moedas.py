def aumentar(x,a,formt=False):
    """
    -> funcao para um aumento percentual
    x: parametro do valor
    a: porcetagem de aumento
    """
    if formt == True:
        return moeda(aumentar(x,a))
    else:
        return x+(x*a/100)


def diminuir(x,d,formt=False):
    """
    ->funcao para diminuir um valor percentual de um numero
    x:parametro de valor
    d:diminuicao percentual
    formt:selecao naturalmente falsa se o numero devera ou nao ser formatado
    """
    if formt == True:
        return moeda(diminuir(x,d))
    else:
        return x - (x * d / 100)


def dobro(x,formt=False):
    if formt == True:
        return moeda(dobro(x))
    else:
        return x * 2


def metade(x,formt=False):
    if formt == True:
        return moeda(metade(x))
    else:
        return x/2


def moeda(x):
    return f'{x:.2f}'

def resumo(x,a=0,d=0):
    """
    x-> Valor que vamos trabalhar
    a-> Valor percentual de aumento
    d-> valor percentual de desconto
    Funcao analisa o valor x e disponibiliza um resumo geral de informaçoes de acordo com os parametros
    """
    print('=-'*15)
    print(f'{"Resumo Do Valor":^30}')
    print('=-'*15)
    print(f'Preco analisado:{moeda(x):>20}R$')
    print(f'Dobro do preco: {dobro(x,True):>20}R$')
    print(f'Metade do preco:{metade(x,True):>20}R$')
    print(f'{a}% de aume =  {aumentar(x,a,True):>20}R$')
    print(f'{d}% de desc =  {diminuir(x,d,True):>20}R$')
    print('=-'*20)





