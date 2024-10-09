from datetime import date
ano = int(input('qual e o ano de nascimento do atleta?'))
idade =date.today().year - ano
azul = '\033[34m'
if idade <= 9:
    print(f'O atleta se enquadra na categoria {azul}MIRIM{azul}')
elif idade > 9 and idade <= 14:
    print(f'O atleta se enquadra na categoria {azul}INFANTIL{azul}')
elif idade > 14 and idade <= 19:
    print(f'O atleta se enquadra na categoria {azul}JUNIOR{azul}')
elif idade == 20:
    print(f'O atleta se enquadra na categoria {azul}SÊNIOR{azul}')
elif idade > 20:
    print(f'O atleta se enquadra na categoria {azul}MASTER{azul}')
