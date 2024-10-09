times = ('PALMEIRAS','GRÊMIO','ATLÉTICO-MG','FLAMENGO','BOTAFOGO','RED BULL BRAGANTINO','FLUMINENSE','ATHLETICO-PR','INTERNACIONAL','FORTALEZA','SÃO PAULO','CUIABA','CORINTHIANS','CRUZEIRO','VASCO','BAHIA','SANTOS','GOIÁS','CORITIBA','AMÉRICA-MG',)
print('o G4 foi definido com os seguintes times')
for x in range(1,5):
    print(f'{x}-{times[x]}')
print(f'o D4 foi fechado da seguinte maneira:')
for y in range(15,20):
    print(f'{y+1}-{times[y]}')
print(f'a lista de todos os times da serie a em ordem alfabetica esta representada a seguir :\n {sorted(times)}')



posicao = str(input('Voce quer verificar a posicao de qual time?')).upper().strip()
print(f'cruzeiro esta na posicao {times.index(posicao)}')
for z in times:
    print(z)