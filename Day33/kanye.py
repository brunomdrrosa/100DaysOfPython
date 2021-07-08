from tkinter import *
import requests


def get_quote():
    kanye_api = requests.get(url="https://api.kanye.rest/")
    kanye_api.raise_for_status()
    dados = kanye_api.json()
    frase = dados["quote"]
    canvas.itemconfig(quote_text, text=frase)

window = Tk()
window.title("Kanye West diz...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 26, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()