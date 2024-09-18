import re
from datetime import datetime
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")


def enviar_notificacion_push(transportista, forma_pago):
    mensajes = {
        "tarjeta": "¡Tu cotización ha sido confirmada y pagada con tarjeta!",
        "contado_retiro": "¡Cotización confirmada! Pago en efectivo al retirar.",
        "contado_entrega": "¡Cotización confirmada! Pago en efectivo contra entrega.",
    }

    mensaje = mensajes.get(forma_pago, "Cotización confirmada.")

    # Corrige el formato del mensaje para evitar problemas de interpolación
    return f"Notificación PUSH enviada al Transportista {transportista}: {mensaje}"


# EMAIL
# No existía la función obtener_desccripcion_pago y la cree abajo pero no se qué debería hacer
# o para que la iba a necesistar el que la hizo
def enviar_email_confirmacion(transportista, email, forma_pago):
    try:
        # Configurar el correo electrónico
        subject = "Confirmación de Cotización Aceptada"
        mensajes = {
            "tarjeta": "Tarjeta",
            "contado_retiro": "Contado Al Retirar",
            "contado_entrega": "Contado Contra Entrega",
        }
        mensaje = mensajes.get(forma_pago)
        body = f"Hola {transportista},\n\nTu cotización ha sido confirmada con la forma de pago: {mensaje}."

        # Crear el mensaje de correo electrónico
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = email  # Usar el email que se pasa como parámetro
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Conectar al servidor SMTP de Gmail
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Iniciar conexión segura
            server.login(EMAIL_USER, EMAIL_PASS)  # Iniciar sesión con el correo y contraseña de aplicación
            text = msg.as_string()
            server.sendmail(EMAIL_USER, email, text)  # Enviar el correo a la dirección pasada como parámetro

        return f"Correo enviado correctamente a {email}."

    except Exception as e:
        return f"Error al enviar el correo: {str(e)}"
