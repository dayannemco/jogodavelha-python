import tkinter as tk
from tkinter import *
from typing import List
from random import randint

modo:List = [0]
simboloJogador:str = ""
nomeX:str = ""
nomeO:str = ""
nomeU:str = ""
num:int = 0
ganhador:str = ""
vitorias:List = []

def menu():
    global janela
    janela = tk.Tk()
    janela.title("JOGO DA VELHA")
    janela.geometry("605x605")
    imagemFundo = tk.PhotoImage(file="tkmenu.png")
    labelFundo = tk.Label(janela, image=imagemFundo)
    labelFundo.place(x=0, y=0)

#Lado do IA
    entradaU = Entry(janela)
    entradaU.place(x=61, y=318, width=180)

#Lado PLayer vs Player
    entradaX = Entry(janela)
    entradaX.place(x=357, y=270, width=180)

    entradaO = Entry(janela)
    entradaO.place(x=357, y=340, width=180)

#Botões
    botaoPlayers = Button(janela, text="1P x 2P", height=9, width=25, fg="white", bg="#73C1FF", highlightbackground="white")
    botaoPlayers.place(x=357,y=388)
    botaoPlayers['command'] = lambda arg1=modo, arg2=botaoPlayers, arg3=entradaU, arg4=entradaX, arg5=entradaO: [alterarModo(arg1, arg2, arg3, arg4, arg5), jogo()]

    botaoPcFacil = Button(janela, text="FÁCIL", height=4, width=25, fg="white", bg="#0F81BA", highlightbackground="white")
    botaoPcFacil.place(x=61, y=388)
    botaoPcFacil['command'] = lambda arg1=modo, arg2=botaoPcFacil, arg3=entradaU, arg4=entradaX, arg5=entradaO: [alterarModo(arg1, arg2, arg3, arg4, arg5), jogo()]

    botaoPcDificil = Button(janela, text="DIFÍCIL", height=4, width=25, fg="white", bg="#73C1FF", highlightcolor="white")
    botaoPcDificil.place(x=61, y=464)
    botaoPcDificil['command'] = lambda arg1=modo, arg2=botaoPcDificil, arg3=entradaU, arg4=entradaX, arg5=entradaO: [alterarModo(arg1, arg2, arg3, arg4, arg5), jogo()]

    janela.mainloop()

def popup(ganhador:str):
    janelinha = tk.Toplevel()
    janelinha.grab_set()
    janelinha.geometry("200x100")
    janelinha.title("JOGO DA VELHA")
    imagemFundo2 = tk.PhotoImage(file="tkpopup.png")
    labelFundoPU = tk.Label(janelinha, image=imagemFundo2)
    labelFundoPU.place(x=0,y=0)
    labelTexto = tk.Label(janelinha, bg="white")
    labelTexto.config(text=ganhador + " ganhou!!")
    labelTexto.place(x=0, y=20, width=200)

    botaoMenu = tk.Button(janelinha, text="MENU", bg="#73C1FF", fg="white")
    botaoMenu.place(x= 40, y=70)
    botaoMenu['command'] = lambda: [janelinha.grab_release(), janela.destroy(), menu()]

    botaoRepetir = tk.Button(janelinha, text="REPETIR", bg="#73C1FF", fg="white")
    botaoRepetir.place(x=100, y=70)
    botaoRepetir['command'] = lambda: [janelinha.grab_release(), jogo()]

    janelinha.mainloop()

def jogo():
    global janela
    janela.destroy()
    janela = Tk()
    janela.title("JOGO DA VELHA")
    janela.geometry("605x605")
    imagemFundo = tk.PhotoImage(file="tkjogo.png")
    labelFundo = tk.Label(janela, image=imagemFundo)
    labelFundo.place(x=0, y=0)
    player = [1]
    vez = Label(janela, text="", bg="white", fg="#431D6C", width=85, pady=12)
    vez.place(x=1,y=40)

    button1 = Button(janela, text=simboloJogador, bg="#431D6C", fg="white", height=6, width=12)
    button1.place(x=109,y=155)
    button2 = Button(janela, text=simboloJogador, bg="#431D6C", fg="white", height=6, width=12)
    button2.place(x=257, y=155)
    button3 = Button(janela, text=simboloJogador, bg="#431D6C", fg="white", height=6, width=12)
    button3.place(x=405, y=155)
    button4 = Button(janela, text=simboloJogador, bg="#431D6C", fg="white", height=6, width=12)
    button4.place(x=109, y=300)
    button5 = Button(janela, text=simboloJogador, bg="#431D6C", fg="white", height=6, width=12)
    button5.place(x=257, y=300)
    button6 = Button(janela, text=simboloJogador, bg="#431D6C", fg="white", height=6, width=12)
    button6.place(x=405, y=300)
    button7 = Button(janela, text=simboloJogador, bg="#431D6C", fg="white", height=6, width=12)
    button7.place(x=109, y=450)
    button8 = Button(janela, text=simboloJogador, bg="#431D6C", fg="white", height=6, width=12)
    button8.place(x=257, y=450)
    button9 = Button(janela, text=simboloJogador, bg="#431D6C", fg="white", height=6, width=12)
    button9.place(x=405, y=450)

    buttonLista = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

    button1['command'] = lambda arg1=player, arg2=button1, arg3=buttonLista, arg4=vez: [alterarTexto(arg1, arg2, arg3), checarResultado(arg3, arg4)]
    button2['command'] = lambda arg1=player, arg2=button2, arg3=buttonLista, arg4=vez: [alterarTexto(arg1, arg2, arg3), checarResultado(arg3, arg4)]
    button3['command'] = lambda arg1=player, arg2=button3, arg3=buttonLista, arg4=vez: [alterarTexto(arg1, arg2, arg3), checarResultado(arg3, arg4)]
    button4['command'] = lambda arg1=player, arg2=button4, arg3=buttonLista, arg4=vez: [alterarTexto(arg1, arg2, arg3), checarResultado(arg3, arg4)]
    button5['command'] = lambda arg1=player, arg2=button5, arg3=buttonLista, arg4=vez: [alterarTexto(arg1, arg2, arg3), checarResultado(arg3, arg4)]
    button6['command'] = lambda arg1=player, arg2=button6, arg3=buttonLista, arg4=vez: [alterarTexto(arg1, arg2, arg3), checarResultado(arg3, arg4)]
    button7['command'] = lambda arg1=player, arg2=button7, arg3=buttonLista, arg4=vez: [alterarTexto(arg1, arg2, arg3), checarResultado(arg3, arg4)]
    button8['command'] = lambda arg1=player, arg2=button8, arg3=buttonLista, arg4=vez: [alterarTexto(arg1, arg2, arg3), checarResultado(arg3, arg4)]
    button9['command'] = lambda arg1=player, arg2=button9, arg3=buttonLista, arg4=vez: [alterarTexto(arg1, arg2, arg3), checarResultado(arg3, arg4)]

    janela.mainloop()

def alterarModo(modo:List, botao:Button, entradaU:Entry, entradaX:Entry, entradaO:Entry):
    global nomeU
    global nomeX
    global nomeO

    if botao['text'] == "FÁCIL":
        modo[0] = 1
        nomeU = entradaU.get()

    elif botao['text'] == "DIFÍCIL":
        modo[0] = 2
        nomeU = entradaU.get()

    elif botao['text'] == "1P x 2P":
        modo[0] = 3
        nomeX = entradaX.get()
        nomeO = entradaO.get()

def alterarTexto(player:List, botao:Button, lista:List[Button]):

    if modo[0] == 3:
        if player[0] == 1:
            if botao['text'] == "":
                botao['text'] = "X"
                player[0] = 2
            else:
                player[0] == 1
        else:
            if botao['text'] == "":
                botao['text'] = "O"
                player[0] = 1
            else:
                player[0] == 2

    if modo[0] == 1 or modo[0] == 2:
        if player[0] == 1:
            if botao['text'] == "":
                botao['text'] = "X"
                player[0] = 2
                #espera alguns segundos
                jogadaPc(player, lista)
            else:
                pass

def jogadaPc(player:List, lista:List[Button]):
    lugaresJogaveis = []
    jogadasPlayer = []
    jogadasPc = []
    empate = "Ninguém"
    score = 0

    for botao in lista:
        if botao['text'] == "":
            lugaresJogaveis.append(botao)
        elif botao['text'] == "X":
            jogadasPlayer.append(botao)
        else:
            jogadasPc.append(botao)

    if lugaresJogaveis == []:
        if ganhador == "":
            popup(empate)

# IA fácil
    lugar = randint(0, len(lugaresJogaveis)-1)
    if modo[0] == 1:
        lugaresJogaveis[lugar]['text'] = "O"
        player[0] = 1
#IA difícil
    elif modo[0] == 2:
        jogada1 = lista[0] or lista[2] or lista[6] or lista[8]
        jogada2 = (lista[1] or lista[3] or lista[5] or lista[7])
        jogada3 = lista[4]
        for jogada in lista:
            if jogada['text'] == "X":
                jogadasPlayer.append(jogada)
            elif jogada['text'] == "O":
                jogadasPc.append(jogada)
            else:
                lugaresJogaveis.append(jogada)

        if jogadasPlayer == [jogada1]:
            lista[4]['text'] = "O"
            player[0] = 1
        elif jogadasPlayer == [jogada2]:
            lista[4]['text'] = "O"
        elif jogadasPlayer == [jogada3]:
            lista[0]['text'] = "O"
        else:
            lugar = randint(0, len(lugaresJogaveis) - 1)
            lugaresJogaveis[lugar]['text'] = "O"
            player[0] = 1

def checarResultado(lista: List[Button], vez:Label):
    global ganhador
    global vitorias
    a = lista[0]['text'] == lista[1]['text'] == lista[2]['text']
    b = lista[0]['text'] == lista[3]['text'] == lista[6]['text']
    c = lista[0]['text'] == lista[4]['text'] == lista[8]['text']
    d = lista[1]['text'] == lista[4]['text'] == lista[7]['text']
    e = lista[2]['text'] == lista[5]['text'] == lista[8]['text']
    f = lista[3]['text'] == lista[4]['text'] == lista[5]['text']
    g = lista[6]['text'] == lista[7]['text'] == lista[8]['text']
    h = lista[2]['text'] == lista[4]['text'] == lista[6]['text']
    vitorias = [a,b,c,d,e,f,g,h]

    if a and lista[0]['text'] != "":
        if lista[0]['text'] == "X":
            if modo[0]==1 or modo[0]==2:
                ganhador = nomeU
            else:
                ganhador = nomeX

        elif lista[0]['text'] == "O":
            if modo[0]==1 or modo[0]==2:
                ganhador = "Pc"
            else:
                ganhador = nomeO

        popup(ganhador)

    elif b and lista[0]['text'] != "":
        if lista[0]['text'] == "X":
            if modo[0] == 1 or modo[0] == 2:
                ganhador = nomeU
            else:
                ganhador = nomeX

        elif lista[0]['text'] == "O":
            if modo[0] == 1 or modo[0] == 2:
                ganhador = "Pc"
            else:
                ganhador = nomeO

        popup(ganhador)

    elif c and lista[0]['text'] != "":
        if lista[0]['text'] == "X":
            if modo[0] == 1 or modo[0] == 2:
                ganhador = nomeU
            else:
                ganhador = nomeX

        elif lista[0]['text'] == "O":
            if modo[0] == 1 or modo[0] == 2:
                ganhador = "Pc"
            else:
                ganhador = nomeO

        popup(ganhador)

    elif d and lista[1]['text'] != "":
        if lista[1]['text'] == "X":
            if modo[0] == 1 or modo[0] == 2:
                ganhador = nomeU
            else:
                ganhador = nomeX

        elif lista[1]['text'] == "O":
            if modo[0] == 1 or modo[0] == 2:
                ganhador = "Pc"
            else:
                ganhador = NomeO

        popup(ganhador)

    elif e and lista[2]['text'] != "":
        if lista[2]['text'] == "X":
            if modo[0] == 1 or modo[0] == 2:
                ganhador = nomeU
            else:
                ganhador = nomeX

        elif lista[2]['text'] == "O":
            if modo[0] == 1 or modo[0] == 2:
                ganhador = "Pc"
            else:
                ganhador = nomeO

        popup(ganhador)

    elif f and lista[3]['text'] != "":
        if lista[3]['text'] == "X":
            if modo[0] == 1 or modo[0] == 2:
                ganhador = nomeU
            else:
                ganhador = nomeX

        elif lista[3]['text'] == "O":
            if modo[0] == 1 or modo[0] == 2:
                ganhador = "Pc"
            else:
                ganhador = nomeO

        popup(ganhador)

    elif g and lista[6]['text'] != "":
        if lista[6]['text'] == "X":
            if modo[0] == 1 or modo[0] == 2:
                ganhador = nomeU
            else:
                ganhador = nomeX

        elif lista[6]['text'] == "O":
            if modo[0] == 1 or modo[0] == 2:
                ganhador = "Pc"
            else:
                ganhador = nomeO

        popup(ganhador)

    elif h and lista[2]['text'] != "":
        if lista[2]['text'] == "X":
            if modo[0] == 1 or modo[0] == 2:
                ganhador = nomeU
            else:
                ganhador = nomeX

        elif lista[2]['text'] == "O":
            if modo[0] == 1 or modo[0] == 2:
                ganhador = "Pc"
            else:
                ganhador = nomeO

        popup(ganhador)

    else:
        global num
        num2:int = num%2
        if modo[0] == 3:
            if num2 == 0:
                if nomeO != "":
                    vez.config(text="É a vez de " + nomeO + ".")
                else:
                    vez.config(text='É a vez do jogador O.')
                num = num + 1

            elif num2 == 1:
                if nomeX != "":
                    vez.config(text="É a vez de " + nomeX + ".")
                else:
                    vez.config(text='É a vez do jogador X.')
                num = num + 1

        elif modo[0] == 1 or modo[0] == 2:
            if nomeU != "":
                vez.config(text="É a vez de " + nomeU + ".")
            else:
                vez.config(text="É sua vez.")
                num = num + 1

menu()