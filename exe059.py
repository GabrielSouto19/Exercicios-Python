menu = 0
valor1 = int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor :'))
while menu != 5:
    azul = '\033[34m'
    limpacor = '\033[m'
    print(f'[1]{azul}Somar{limpacor}: \n[2]{azul}Multiplicar{limpacor}:\n[3]{azul}Maior{limpacor}:\n[4]{azul}Novos numeros{limpacor}:\n[5]{azul}Sair do programa{limpacor}:')
    menu = int(input('Digite o comando correspondente:'))
    if menu == 1:
        print(f'A soma correspondente entre o valor {valor1} e {valor2} e igual a {valor1 + valor2}!')
    elif menu == 2:
        print(f'A multiplicacao correspondente entre o valor {valor1} e {valor2} e igual a {valor1 * valor2}')
    elif menu == 3:
        if valor1 > valor2:
            print(f'o maior valor foi {valor1}')
        else:
            print(f'o maior valor foi {valor2}')
    elif menu == 4:
        valor1 = int(input('Digite o novo primeiro valor:'))
        valor2 = int(input('Digite o novo segundo valor :'))

print('Programa finalizado!')

# maneira alternativa de mostrar os numeros em python uma linha apos a outra
# print('''[1]
# [2]
# [3]
# [4]''')
