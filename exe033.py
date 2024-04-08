numero1 = int(input('digite um numero'))
numero2 = int(input('digite um numero'))
numero3 = int(input('digite um numero'))
if numero1 > numero2 and numero1 > numero3:
    print(f'{numero1} é o maior numero')
elif numero2 > numero1 and numero2 > numero3:
    print(f'{numero2} é o maior numero')
elif numero3 > numero2 and numero3 > numero1:
    print(f'{numero3} é o maior numero')

if numero1 < numero2 and numero1 < numero3:
    print(f'{numero1} é o menor numero')
elif numero2 < numero1 and numero2 < numero3:
    print(f'{numero2} é o menor numero')
elif numero3 < numero2 and numero3 < numero1:
    print(f'{numero3} é o menor numero')

