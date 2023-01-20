from email.message import EmailMessage # importamos desde message que está entro del objeto email a EmailMessage que nos permitirá estructurar un mensaje tipo email
import ssl
import smtplib
email_sender = 'findanprogram@gmail.com'
email_password = 'qccjgmppuofciyzu'

email_receiver = 'da.jaramim@gmail.com'

subject = "Correo de prueba"
body = """
Este es un correo de prueba para practicar con el lenguaje
de programación Python.
"""

em = EmailMessage() #instancia de lo que importamos arriba
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
#smtp es un protocolo de red para intercambiar correos electrónicos entre computadores y otros dispositivos
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: #ssl permite que una transferencia de datos sea segura
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())