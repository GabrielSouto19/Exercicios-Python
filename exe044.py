prod = float(input('qual e o preco do produto?'))
forpag = int(input('qual vai ser a forma de pagamento:\n 1- A vista no dinheiro\n 2- A vista no cartao \n 3- Em ate 2 vezes no cartao \n 3- 3 vezes ou mais no cartao \n'))
if forpag == 1:
    prod = prod - (prod *10/100)
    print(f'Parabens voce ganhou um desconto de 10%\nPreco final R${prod:.2f}')
elif forpag == 2:
    prod = prod - (prod *5/100)
    print(f'Parabens voce ganhou um desconto de 5%\nPreco final R${prod:.2f}')
elif forpag == 3:
    print(f'Obrigado por comprar conosco! Volte sempre!!!\n Preco final R${prod:.2f}')
elif forpag == 4:
    prod = prod + (prod*20/100)
    print(f'o seu pao duro, pra ficar esperto vai pagar 20% de juros.\n Preco final R${prod:.2f}')
