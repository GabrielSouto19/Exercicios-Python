numeros = ('zero','um','dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove' ,'dez' ,'onze' ,'doze' ,'treze' ,'quatorze' ,'quinze' ,'dezesseis', 'dezessete' ,'dezoito', 'dezenove' ,'vinte')
while True:
    num = int(input('Escolha um numero de 0 a 20:'))
    while num > 20:
        print('atencao escolha um numero valido!')
        num = int(input('Escolha um numero de 0 a 20:'))
    print(f'O numero por externso é {numeros[num]}')
    
