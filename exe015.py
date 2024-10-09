km   = float(input('quantos kms foram rodados?'))
dias = int(input('quantos dias foram gastos? '))
diaria = 60
rodados = 0.15
totpag = (km * rodados) + (dias * diaria)
print(f'o total a pagar foi {totpag} R$')
