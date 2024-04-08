def notas(*num,sit=False):
    """
    funcao para analisar notas
    para num: notas do aluno
    sit = situaçao naturalmente falsa
    return = retorna uma biblioteca com dados gerais obtidos a partir da nota
    """
    r = {}
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = (sum(num) / len(num))
    if sit == True:
        if r['media'] < 6:
            print(f'Media {r['media']:.2f} sit:RUIM')
            r['sit'] = 'RUIM'
        elif r['media'] > 6 and r['media'] < 7.5:
            r['sit'] = 'RAZOAVEL'
            print(f'Media {r['media']:.2f} sit: RAZOAVEL!')
        else:
            r['sit'] = 'BOA'
            print(f'Media {r['media']:.2f} sit:BOA')
    return r
#programa principal
resp = notas(9.5,7.5,5.5,10,5)
print(resp)
help(notas)
