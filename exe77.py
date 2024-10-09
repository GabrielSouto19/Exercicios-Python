palavras = ('python','aprender','programacao','word','excel','celular','curso','video','cachorro','gato','papagaio','girafa','marketing','digital','vender','astronomia','rock','guitarra','jack','black','filme',)
cont = 0
for i in range(0,len(palavras)):
    print(f'\nNa palavra {palavras[i]} temos ',)
    for v in palavras[i]:
        if v in 'aeiou':
            print(f'{v}',end='')
