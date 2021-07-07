from datetime import datetime
import pandas
import random
import smtplib

# Insira o seu e-mail dentro da string
MEU_EMAIL = "brunomdr46@gmail.com"

# Insira a sua senha dentro da string
MINHA_SENHA = ""

hoje = (datetime.now().month, datetime.now().day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if hoje in birthdays_dict:
    aniversariante = birthdays_dict[hoje]
    diretorio = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(diretorio) as arquivo:
        conteudo = arquivo.read()
        conteudo = conteudo.replace("[NAME]", aniversariante["name"])

    with smtplib.SMTP("smtp.gmail.com") as conexao:
        conexao.starttls()
        conexao.login(user=MEU_EMAIL, password=MINHA_SENHA)
        conexao.sendmail(
            from_addr=MEU_EMAIL,
            to_addrs=aniversariante["email"],
            msg=f"Subject: Feliz aniversario!\n\n{conteudo}"
        )