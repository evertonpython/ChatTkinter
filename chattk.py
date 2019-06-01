#coding=utf-8
from tkinter import *

def conversa():
    print("Funcionou")
    resp = ['oie', 'tudo sim, e com você?', 'infelizmente kk'] ###### RESPOSTAS RELATIVAS ÁS PERGUNTAS ########
    n2 = str(edEu.get())
    lb["text"] = resp


    if n2 == 'ola' :
        lb["text"] = resp[0]
    elif n2 == 'tudo bem?':
        lb["text"] = resp[1]
    elif n2 == 'tudo, esta chovendo ai?':
        lb["text"] = resp[2]

def sair():
    quit()


janela = Tk()

lb2 = Label(janela, text="Digite sua mensagem:", width=20)
lb2.place(x=10, y=50)

lbUser = Label(janela, text="Usuário:", width=20)
lbUser.place(x=10, y=100)

edEu = Entry(janela, bg="white", fg="black")
edEu.place(x=200, y=50)

bt = Button(janela, text="Enviar", width=5, command=conversa )
bt.place(x=400, y=50)

btSair = Button(janela, text="Sair", width=5, command=sair)
btSair.place(x=400, y=134)

# LABEL QUE VAI APARECER A RESPOSTA DO USUÁRIO
lb = Label(janela, text="",width=30, bg="white", fg="red")
lb.place(x=200, y=100)
#                    CopyWrite   by Everton            #
lbCred = Label(janela, text="by - Everton Sousa", width=20, bg="black", fg="white")
lbCred.place(x=150, y=145)

janela["bg"] = "black"

janela.title("Chat - Off")

janela.geometry("470x170+200+200")

janela.mainloop()
