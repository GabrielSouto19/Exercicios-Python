from datetime import date
nasc = int(input('qual e o seu ano de nascimento?'))
idade = date.today().year - nasc
if idade == 18:
    print('E hora de se alistar')
elif idade > 18:
    print(f'ja passou do seu tempo filhao viro refratario, era pra tu ter ido a {idade-18} anos ')

else:
    print(f'voce ainda vai se alistar, falta {18-idade}anos lek ')
