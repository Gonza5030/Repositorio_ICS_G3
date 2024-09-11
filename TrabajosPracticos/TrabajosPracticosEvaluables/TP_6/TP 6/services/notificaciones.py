import re
from datetime import datetime


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
def enviar_email_confirmacion(transportista, forma_pago):
    mensajes = {
        "tarjeta": "Tarjeta.",
        "contado_retiro": "Efectivo al retirar.",
        "contado_entrega": "Efectivo contra entrega.",
    }

    mensaje = mensajes.get(forma_pago, "Cotización confirmada.")

    # Corrige el formato del mensaje para evitar problemas de interpolación
    return f"Mail de confirmación enviado al Transportista {transportista}: Método de pago: {mensaje}"
