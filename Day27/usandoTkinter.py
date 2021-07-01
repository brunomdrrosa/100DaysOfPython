from tkinter import *

window = Tk()
window.title("Primeiro programa GUI")
window.minsize(width=500, height=300)

# Texto
texto = Label(text="Eu sou um texto", font=("Arial", 28, "bold"))
texto.pack()

# Botão
def botao_clicado():
    print("Eu fui clicado")
    texto_novo = input.get()
    texto.config(text=texto_novo)

botao = Button(text="Clique-me", command=botao_clicado)
botao.pack()

# Entrada
input = Entry(width=20)
input.pack()
print(input.get())

window.mainloop()

