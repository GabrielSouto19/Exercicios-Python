from datetime import date#e possivel usar o escopo de importaçao , para que nao seja necessario importar uma biblioteca para o programa inteiro,economiza memoria


anoatual = date.today().year
def voto(n):
    idade = anoatual - n
    if idade >=18 and idade < 65:
        return f'Com {idade} anos o voto é :OBRIGATORIO'
    elif idade >= 16 and idade < 18 or idade >= 65:
        return f'com {idade} anos o voto é :OPCIONAL'
    else:
        return f'Com {idade} anos o voto é :NEGADO'


anonasc = int(input('Digite seu ano de nascimento:'))
res = voto(anonasc)
print(res)
