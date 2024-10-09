def leiadinheiro(x):
    valido = False
    while not valido:
        entrada = str(input(x)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[31mErro!Valor invalido \033[m')
        else:
            valido = True
            return float(entrada)