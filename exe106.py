c = ['\033[0;0m', #limpacor0
    '\033[31m',#vermelho1
    '\033[32m', #verde2
    '\033[34m', # azul3
    '\033[36m', #ciano4
    '\033[35m', #magenta5
    '\033[33m', #amarelo6
    '\033[30m' ,# preto7
    '\033[37m' ,#branco8
    '\033[1m',#negrito9
    '\033[2m',#reverso10
    '\033[40m',#fundo preto11
    '\033[41m',#fundo vermelho12
    '\033[42m', #fundo verde13
    '\033[43m',#fundo amarelo14
    '\033[44m', #fundo azul15
    '\033[45m' ,#fundo magenta16
    '\033[7;40m',#fundo branco17
    '\033[46m',#funco ciano18
]

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',7)
    print(c[15])
    help(com)
    print(c[0])

def titulo(msg,cor=0):
    tam = len(msg)+4
    print(c[cor],end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0],end='')


comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp',cor=12)
    comando = str(input('Comando ou Biblioteca:>'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Ate Logo!',12)


