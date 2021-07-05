from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
carta_atual = {}
aprender = {}

try:
    dados = pandas.read_csv("data/palavras_para_aprender.csv")
except FileNotFoundError:
    dados_originais = pandas.read_csv("data/palavras_portugues.csv")
    aprender = dados_originais.to_dict(orient="records")
else:
    aprender = dados.to_dict(orient="records")


def proxima_carta():
    global carta_atual, timer
    janela.after_cancel(timer)
    carta_atual = random.choice(aprender)
    canvas.itemconfig(titulo_carta, text="Inglês", fill="black")
    canvas.itemconfig(palavra_carta, text=carta_atual["Inglês"], fill="black")
    canvas.itemconfig(fundo_carta, image=carta_frente)
    timer = janela.after(3000, func=virar_carta)

def virar_carta():
    canvas.itemconfig(titulo_carta, text="Português", fill="white")
    canvas.itemconfig(palavra_carta, text=carta_atual["Português"], fill="white")
    canvas.itemconfig(fundo_carta, image=carta_atras)

def acertada():
    aprender.remove(carta_atual)
    dados = pandas.DataFrame(aprender)
    dados.to_csv("data/palavras_para_aprender.csv", index=False)
    proxima_carta()

# CRIAÇÃO DA INTERFACE
janela = Tk()
janela.title("Flashcard")
janela.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = janela.after(3000, func=virar_carta)

canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)

carta_frente = PhotoImage(file="images/card_front.png")
carta_atras = PhotoImage(file="images/card_back.png")
fundo_carta = canvas.create_image(400, 263, image=carta_frente)
titulo_carta = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
palavra_carta = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

imagem_errado = PhotoImage(file="images/wrong.png")
botao_errado = Button(image=imagem_errado, highlightthickness=0, command=proxima_carta)
botao_errado.grid(row=1, column=0)

imagem_certo = PhotoImage(file="images/right.png")
botao_certo = Button(image=imagem_certo, highlightthickness=0, command=acertada)
botao_certo.grid(row=1, column=1)

proxima_carta()

janela.mainloop()