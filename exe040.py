nota1 = float(input('qual foi sua primeira nota:'))
nota2 = float(input('qual foi sua segunda nota:'))
media = (nota1+nota2)/2
if media < 5.0:
    print('Reprovado')
elif media >= 5.0 and media < 7.0:
    print('voce esta de recuperaçao')
elif media >= 7:
    print('liberdade cantou , aprovado lek ')
