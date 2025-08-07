#colocando a biblioteca tkinter
from tkinter import *
from tkinter import Tk

#variável cor
cor1="#232933"
cor2 = "#f8f8f2"
cor3 = "#5a6585"
cor4 = "#0f6ce6c8"
cor5 = "#fa9090df"

#colocando o tkinter na janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("250x338")
janela.config(bg=cor1)

#frames da calculadora
frame_tela = Frame (janela, width=250, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame (janela, width=250, height=288, bg=cor3)
frame_corpo.grid(row=1, column=0)

#criação de botões
botao1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao1.place(x=0, y=0)

botao2 = Button(frame_corpo, text="%", width=5, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao2.place(x=100, y=0)

botao3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao3.place(x=177, y=0)

botao4 = Button(frame_corpo, text="7", width=11, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao4.place(x=0, y=52)

botao5 = Button(frame_corpo, text="8", width=11, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao5.place(x=59, y=52)

botao6 = Button(frame_corpo, text="9", width=11, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao6.place(x=118, y=52)

botao7 = Button(frame_corpo, text="x", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao7.place(x=177, y=52)

botao8 = Button(frame_corpo, text="4", width=11, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao8.place(x=0, y=104)

botao9 = Button(frame_corpo, text="5", width=11, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao9.place(x=59, y=104)

botao10 = Button(frame_corpo, text="6", width=11, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao10.place(x=118, y=104)

botao11 = Button(frame_corpo, text="-", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao11.place(x=177, y=104)

botao12 = Button(frame_corpo, text="1", width=11, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao12.place(x=0, y=156)

botao13 = Button(frame_corpo, text="2", width=11, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao13.place(x=59, y=156)

botao14 = Button(frame_corpo, text="3", width=11, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao14.place(x=118, y=156)

botao15 = Button(frame_corpo, text="+", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao15.place(x=177, y=156)

botao16 = Button(frame_corpo, text="0", width=11, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao16.place(x=0, y=208)

botao17 = Button(frame_corpo, text=".", width=5, height=2, bg=cor3, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
botao17.place(x=118, y=208)

botao18 = Button(frame_corpo, text="=", width=5, height=2, bg=cor5, fg=cor2, font=("Ivy 13 Bold"), relief=RAISED, overrelief=RIDGE)
botao18.place(x=177, y=208)

janela.mainloop()
