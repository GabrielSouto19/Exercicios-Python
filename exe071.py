print('='*30)
print(f'{'BANCO MAGALIO':^30}')
saque = int(input('qual sera o valor de saque?'))
resto = saque
oncinha = pilinha = davint = deizin = 0#nota de cinquenta
# o caixa so tera cedulas no valor de 50,20,10,1
while resto != 0:
    if resto > 50:
        oncinha += resto // 50
        resto = resto % 50
    if resto > 20 and resto < 50:
        davint = resto // 20
        resto = resto % 20
    if resto > 10 and resto < 20:
        deizin = resto // 10
        resto = resto % 10
    if resto >= 1 and resto < 10:
        pilinha = resto // 1
        resto = resto % 1
# print(f'o numero de cedulas de 50 foi de {oncinha} , mais {davint} notas de vinte , mais {deizin} notas de 10 mais {pilinha} notas de 1 ')
print(f'saque autorizado! voce recebera: \n{oncinha} notas de 50R$\n{davint} notas de 20R$\n{deizin} notas de 10R$\n{pilinha} notas de 1R$')