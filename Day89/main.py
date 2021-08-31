from tkinter import *
import copy

OCCUR = False


# Recursive loop to check if typing stopped then clear the textbox
def disappear():
    global current_length, text, window, OCCUR
    new_length = len(text.get("1.0", "end"))
    if not OCCUR:
        if new_length == current_length:
            OCCUR = True
            # Time to wait after typing stops to make the text disappear in milliseconds
            window.after(3000, disappear)
    elif new_length == current_length and OCCUR:
        # Disappear the text from the textbox
        text.delete("1.0", "end")
        current_length = len(text.get("1.0", "end"))
        OCCUR = False
        disappear()
    elif OCCUR:
        current_length = copy.copy(new_length)
        OCCUR = False
        disappear()


# Main
window = Tk()
window.title('Não pare de digitar')
window.minsize(width=500, height=500)
window.config(padx=10, pady=10, bg='#4682b4')

label = Label(text='Se você parar de digitar por 3 segundos, o texto irá DESAPARECER!', wraplength=980,
                      justify='center', font="Times 15")
label.grid(row=0, column=0, pady=10)

text = Text(window, height=20, width=50, font="Courier 15")
text.grid(row=1, column=0, pady=10)

current_length = len(text.get("1.0", "end"))

disappear()

window.mainloop()
