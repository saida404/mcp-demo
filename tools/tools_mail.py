import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os   
from dotenv import load_dotenv
from tools.pomocne.pomocna import handle_tool_errors

load_dotenv()

GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")


@handle_tool_errors
def tools_posalji_mail(tip_racuna: str, mjesec: str, godina: int):
    
    subject = f"Prijava greške - dupli računa za {tip_racuna} {mjesec}/{godina}"
    
    body = f"""
Poštovani,

Obraćam Vam se u vezi sa računom koji sam primila za {mjesec}/{godina}.

Primijetila sam da ste mi proslijedili dva računa za {tip_racuna} 
za isti period, što smatram greškom.

Molim Vas da provjerite da li su ova dva računa zaista potrebna ili da li je došlo do greške.

S poštovanjem,
Saida
    """

    msg = MIMEMultipart()
    msg["From"] = GMAIL_ADDRESS
    msg["To"] = GMAIL_ADDRESS
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_ADDRESS, GMAIL_ADDRESS, msg.as_string())

    return {"message": f"Mail uspješno poslan na {GMAIL_ADDRESS}"}