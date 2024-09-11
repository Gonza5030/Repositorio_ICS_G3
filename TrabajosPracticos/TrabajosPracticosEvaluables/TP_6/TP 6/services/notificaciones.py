import re
from datetime import datetime

def enviar_notificacion_push(transportista, forma_pago):
    mensajes = {
        "tarjeta": "¡Tu cotización ha sido confirmada y pagada con tarjeta!",
        "contado_retiro": "¡Cotización confirmada! Pago en efectivo al retirar.",
        "contado_entrega": "¡Cotización confirmada! Pago en efectivo contra entrega."
    }
    
    mensaje = mensajes.get(forma_pago, "Cotización confirmada.")
    
    # Corrige el formato del mensaje para evitar problemas de interpolación
    return f"Notificación PUSH: {mensaje} Transportista: {transportista.nombre}"


def enviar_notificacion_push(transportista, forma_pago):
    mensajes = {
        "tarjeta": "¡Tu cotización ha sido confirmada y pagada con tarjeta!",
        "contado_retiro": "¡Cotización confirmada! Pago en efectivo al retirar.",
        "contado_entrega": "¡Cotización confirmada! Pago en efectivo contra entrega."
    }
    
    mensaje = mensajes.get(forma_pago, "Cotización confirmada.")
    return "Notificación PUSH: {mensaje} Transportista: {transportista.nombre}"


def enviar_email_confirmacion(transportista, forma_pago):
    descripcion = obtener_descripcion_pago(forma_pago)
