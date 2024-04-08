expressao = str(input('Digite uma expressao matematica:'))
# abrindo = expressao.count('(')
# fechando = expressao.count(')')
# if abrindo == fechando:
#     print('Sua expressao esta correta !parabens !!!')
# else:
#     print('Expressao incorreta!')
# pequeno problema na minha resulucao , se houver a seguinte expressao:a) + b( na logica esta correta porem esta incorreta esta funcao
pilha = []
for s in expressao:
    if s == '(':
        pilha.append('(')
    elif s == ')':
        if len(pilha) >0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) > 0:
    print('sua expressao esta incorreta')
else:
    print('parabens sua expressao e valida!')

