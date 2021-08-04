from flask import Flask
app = Flask(__name__)
import random

random_number = random.randint(0, 9)
print(random_number)

@app.route('/')
def home():
    return '<h1>Adivinhe o número de 0 a 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="GIF de números de 0 a 9">' \

@app.route("/<int:palpite>")
def guess_number(palpite):
    if palpite > random_number:
        return "<h1 style='color: purple'>Número muito alto, tente novamente!</h1>" \
               "<img src='https://media.giphy.com/media/vexp4GOO5r0OI/giphy.gif'>"

    elif palpite < random_number:
        return "<h1 style='color: red'>Número muito baixo, tente novamente!</h1>"\
               "<img src='https://media.giphy.com/media/j5bsZqX1KTKngMyu90/giphy.gif'>"
    else:
        return '<h1>Você acertou, parabéns!</h1>' \
               '<img src="https://media.giphy.com/media/ummeQH0c3jdm2o3Olp/giphy.gif" alt="GIF com um senhor gritando "Bingo"">' \

if __name__ == "__main__":
     app.run(debug=True)
