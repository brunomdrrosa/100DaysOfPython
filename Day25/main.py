import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Jogo dos estados do Brasil")
imagem = "C:/Users/bruno/OneDrive/Área de Trabalho/100DaysOfPython/Day25/mapa_brasil.gif"
turtle.addshape(imagem)
turtle.shape(imagem)

dados = pd.read_csv("C:/Users/bruno/OneDrive/Área de Trabalho/100DaysOfPython/Day25/estados.csv")
todos_estados = dados.estado.to_list()
estados_adivinhados = []

# Função para descobrir as coordenadas dos estados na imagem
# def get_cords(x, y):
#     print(x, y)

# turtle.onscreenclick(get_cords)
# turtle.mainloop()

while len(estados_adivinhados) < 26:
    resposta = screen.textinput(title=f"{len(estados_adivinhados)}/26 estados corretos", prompt="Qual o nome do estado que está faltando?")

    if resposta == "Sair":
        estados_faltantes = []
        for estado in todos_estados:
            if estado not in estados_adivinhados:
                estados_faltantes.append(estado)
        print(estados_faltantes)
        break
    if resposta in todos_estados:
        estados_adivinhados.append(resposta)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        dados_estado = dados[dados.estado == resposta]
        t.goto(int(dados_estado.x), int(dados_estado.y))
        t.write(resposta)