from tkinter import *

def km_para_milhas():
    km = float(km_input.get())
    milhas = round(km / 1.609, 2)
    milhas_resultado.config(text=f"{milhas}")

janela = Tk()
janela.title("Conversor de Quilômetros para Milhas")
janela.config(padx=20, pady=20)

km_input = Entry(width=7)
km_input.grid(column=1, row=0)

km_label = Label(text="Quilômetros")
km_label.grid(column=2, row=0)

e_igual_a = Label(text="é igual a")
e_igual_a.grid(column=0, row=1)

milhas_resultado = Label(text="0")
milhas_resultado.grid(column=1, row=1)

milhas_label = Label(text="Milhas")
milhas_label.grid(column=2, row=1)

botao_calcular = Button(text="Calcular", command=km_para_milhas)
botao_calcular.grid(column=1, row=2)

janela.mainloop()