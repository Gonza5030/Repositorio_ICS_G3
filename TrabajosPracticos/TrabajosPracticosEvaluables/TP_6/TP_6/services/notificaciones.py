# services/notificaciones.py

def enviar_notificacion_push(transportista, forma_pago):
    print(f"Notificación PUSH: Cotización confirmada para {transportista.nombre}. Forma de pago: {forma_pago}")

def enviar_email_confirmacion(transportista, forma_pago):
    print(f"Email: Confirmación enviada a {transportista.nombre}. Forma de pago: {forma_pago}")
