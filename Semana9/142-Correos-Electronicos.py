import smtplib #Esta biblioteca me permite hacer solicitudes a un servidor
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("Hola, este es un mensaje automatico de Python")
msg["Subject"] = "Mensaje Automatico"
msg["From"] = "feroroxom@gmail.com"
msg["To"] = "campestrefer@gmail.com"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp: #El host y pueryto que alojaran mi mensaje
    smtp.login("feroroxom@gmail.com", "gxmg clxr icvb infe")
    smtp.send_message(msg)

print("Correo enviado automaticamente")