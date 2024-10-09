import requests
from tkinter import *
#primeira coisa e criar essa janela inicial
#tk() codigo que cria a tela
def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto

#ideal a gente desenhar um esboco para visualizar como ficara a nossa tela
#pedaco de texto dentro da janela fazemos com label
# pegar_cotacoes()

janela = Tk()
janela.title('Cotação atual das moedas')#edita o titulo que vem inicialmente com tk
janela.geometry("400x400")
texto_orientacao = Label(janela,text='Clique no botao para exibir a cotaçao das moedas ')#dentro dos parenteses temos que espicificar onde sera exibido nossa caixa de texto qual janela
texto_orientacao.grid(column=0,row=0,padx=10,pady=10)#podemos testar diversas dimensoes para ver qual se adapta melhor

botao = Button(janela,text='Buscar cotações Dolar/Euro/BTC',command=pegar_cotacoes)#sempre que formos criar um botao usamos o methodo Button que e do tk inter , primeiro dizemos em que janela que o botao vai ser inserido e depois o conteudo e por ultimo o command que vai ser oque ele vai fazer quando o botao for clickado , geralmente e o nome de uma funcao obs nao passar o parentes no final para que a funcao so seja executado quando o botao for pressionado , se colocarmos o parentese a funcao sera executada sozinha sem comando
botao.grid(column=0,row=1,padx=10,pady=10)

texto_cotacoes = Label(janela,text='')
texto_cotacoes.grid(column=0,row=2,padx=10,pady=10)


#janela.mainloop()ele garente que a janela continue sendo exibida
#onde sera posicionado o texto ?  primeiro criamos o texto e depois escolhemos a posicao com o grid
#como aumentar o espaco entre os items, temos o parametro padx e pady e ai vamos testando valores
#como aumentar o tamanho da janela : temos a funca geometry e passamos o tamanho como string geometry("450x200")exemplo
