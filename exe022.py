nomecom = str(input('qual e o seu nome completo?')).strip()
print(f'seu nome em letras maiusculas é {nomecom.upper()}')
print(f'seu nome em letras minusculas é {nomecom.lower()}')
print(len(nomecom)-nomecom.count(' '))
divisao = nomecom.split()
print(len(divisao[0]+divisao[1]+divisao[2]+divisao[3]))
print(len(divisao[0]))
print(nomecom.find(' '))# jeito alternativo do guanabara