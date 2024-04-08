def leiadinheiro(x):
    """
    ---> valida somente valores monetarios
    x -> parametro que trabalha com o valor
    """
    if x.isnumeric() == False:
        while True:
            x = str(input(f'\033[31mErro :{x} e invalido! Digite um valor valido!\033[m'))
            if x.isnumeric():
                x = int(x)
                print('\033[32mDado validado !')
                break
    elif x.isnumeric():
        x = int(x)
        return '\033[32mDado validado com sucesso!'

