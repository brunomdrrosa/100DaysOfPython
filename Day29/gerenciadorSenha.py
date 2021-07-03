from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gerar_senha():
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letras_senha = [choice(letras) for _ in range(randint(8, 10))]
    simbolos_senha = [choice(simbolos) for _ in range(randint(2, 4))]
    numeros_senha = [choice(numeros) for _ in range(randint(2, 4))]

    senha_lista = letras_senha + simbolos_senha + numeros_senha
    shuffle(senha_lista)

    senha = "".join(senha_lista)
    if len(senha_input.get()) == 0:
        senha_input.insert(0, senha)
    else:
        senha_input.delete(0, END)
        senha_input.insert(0, senha)
    pyperclip.copy(senha)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def salvar():
    
    site = site_input.get()
    login = login_input.get()
    senha = senha_input.get()

    if len(site) == 0 or len(senha) == 0:
        messagebox.showinfo(title="Ops...", message="Você deixou algum campo vazio.")
    else:
        alerta = messagebox.askokcancel(title=site, message=f"Os seguintes dados foram inseridos: \nLogin: {login} \nSenha: {senha} \nVocê quer adicionar os dados no arquivo?")
        if alerta:
            with open("dados.txt", "a") as arquivo:
                arquivo.write(f"{site} | {login} | {senha}\n")
                site_input.delete(0, END)
                senha_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
janela = Tk()
janela.title("Gerenciador de senhas")
janela.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=logo)
canvas.grid(row=0, column=1)

# Textos
site_texto = Label(text="Site:")
site_texto.grid(column=0, row=1)
login_texto = Label(text="Login:")
login_texto.grid(row=2, column=0)
senha_texto = Label(text="Senha:")
senha_texto.grid(row=3, column=0)

# Inputs
site_input = Entry()
site_input.grid(column=1, row=1, columnspan=2, sticky="EW")
site_input.focus()
login_input = Entry()
login_input.grid(column=1, row=2, columnspan=2, sticky="EW")
login_input.insert(0, "brunomdr46@gmail.com")
senha_input = Entry()
senha_input.grid(column=1, row=3, sticky="EW")

# Botões
gerar_senha = Button(text="Gerar uma senha", command=gerar_senha)
gerar_senha.grid(column=2, row=3, sticky="EW")
botao_adicionar = Button(text="Adicionar", width=35, command=salvar)
botao_adicionar.grid(column=1, row=4, columnspan=2, sticky="EW")

janela.mainloop()