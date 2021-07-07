import smtplib
import datetime as dt
import random

# Insira o seu e-mail dentro da string
MEU_EMAIL = "brunomdr46@gmail.com"

# Insira a sua senha dentro da string
MINHA_SENHA = ""

hoje = dt.datetime.now()
dia_da_semana = hoje.weekday()
if dia_da_semana == 0:
    with open("frases.txt") as arquivo_frases:
        todas_frases = arquivo_frases.readlines()
        frase = random.choice(todas_frases)

    print(frase)
    with smtplib.SMTP("smtp.gmail.com") as conexao:
        conexao.starttls()
        conexao.login(user=MEU_EMAIL, password=MINHA_SENHA)
        conexao.sendmail(
            from_addr=MEU_EMAIL,
            to_addrs=MEU_EMAIL,
            msg=f"Subject: Frase motivacional de Segunda\n\n{frase}"
        )