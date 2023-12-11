import smtplib
import ssl
import mimetypes
from email.message import EmailMessage

password = open('senha', 'r').read()
from_email = "ricardotonholli@gmail.com"
to_email = "ricardotonholli@gmail.com"
subject = "Automação de Planilha"
body = "Segue a planilha com o gráfico"

message = EmailMessage()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject

message.set_content(body)
safe = ssl.create_default_context()

anexo = "test.xlsx"
mine_type, mine_subtype = mimetypes.guess_type(anexo)[0].split('/')
with open(anexo, "rb") as a:
    message.add_attachment(
        a.read(),
        maintupe = mine_type,
        subtype = mine_subtype,
        filename = anexo
    )
with smtplib.SMTP_SSL("smtp.gmail.com" , 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail (
        from_email,
        to_email,
        message.as_string()
    )

