from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeticoes = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reiniciar():
    janela.after_cancel(timer)
    canvas.itemconfig(timer_texto, text="00:00")
    texto_timer.config(text="Timer")
    check.config(text="")
    global repeticoes
    repeticoes = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def iniciar_tempo():
    global repeticoes
    repeticoes += 1

    trabalhar_segundos = WORK_MIN * 60
    intervalo_pequeno_segundos = SHORT_BREAK_MIN * 60
    intervalo_grande_segundos = LONG_BREAK_MIN * 60

    if repeticoes % 8 == 0:
        contador(intervalo_grande_segundos)
        texto_timer.config(text="Descanso", fg=RED)
    elif repeticoes % 2 == 0:
        contador(intervalo_pequeno_segundos)
        texto_timer.config(text="Descanso", fg=PINK)
    else:
        contador(trabalhar_segundos)
        texto_timer.config(text="Trabalhar", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def contador(contagem):

    contagem_min = math.floor(contagem / 60)
    contagem_sec = contagem % 60
    if contagem_sec < 10:
        contagem_sec = f"0{contagem_sec}"

    canvas.itemconfig(timer_texto, text=f"{contagem_min}:{contagem_sec}")
    if contagem > 0:
        global timer
        timer = janela.after(1000, contador, contagem - 1)
    else:
        iniciar_tempo()
        checks = ""
        sessoes = math.floor(repeticoes/2)
        for _ in range(sessoes):
            checks += "✅"
        check.config(text=checks)

# ---------------------------- UI SETUP ------------------------------- #
janela = Tk()
janela.title("Pomodoro")
janela.config(padx=100, pady=50, bg=YELLOW)

texto_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
texto_timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
imagem_tomate = PhotoImage(file="C:/Users/bruno/OneDrive/Área de Trabalho/100DaysOfPython/Day28/tomate.png")
canvas.create_image(100, 112, image=imagem_tomate)
timer_texto = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

botao_inicial = Button(text="Iniciar", highlightthickness=0, command=iniciar_tempo)
botao_inicial.grid(column=0, row=2)

botao_reset = Button(text="Reiniciar", highlightthickness=0, command=reiniciar)
botao_reset.grid(column=2, row=2)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)

janela.mainloop()