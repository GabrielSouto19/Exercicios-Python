frase = str(input('digite uma frase qualquer')).strip()
quebrado = frase.split()
print(f'a letra "a" aparece {frase.lower().count('a')}x')
print(f'a primeira letra "a" aparece na posicao {frase.find('a')}')
print(f'a ultima letra "a" aparece em {frase.rfind('a')}')

