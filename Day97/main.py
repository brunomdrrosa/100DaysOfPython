import os
import smtplib
import datetime 

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

todayDate = datetime.date.today()
if todayDate.day == 1:
  with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
       from_addr=MY_EMAIL,
       to_addrs="brunomdr46@gmail.com",
       msg=f"Subject:Aviso para atualizar LinkedIn!\nNão se esqueça de atualizar o perfil no LinkedIn com os cursos realizados".encode('utf-8')
  )
