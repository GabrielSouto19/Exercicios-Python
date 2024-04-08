nome = str(input('digite seu nome completo'))
lista = nome.split()
primeironome = lista[0]
sobrenome = len(lista)
print(f'Bem vindo {primeironome.title()}!')
print(f'Muito prazer Sr {lista[sobrenome - 1].title()}!')
# consegui fazer sozinho
