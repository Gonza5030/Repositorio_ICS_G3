    # notifications.py
def enviar_notificacion_push(transportista):
    print(f"Notificación PUSH enviada a {transportista.nombre}: La cotización ha sido confirmada.")

def enviar_correo(transportista):
    print(f"Correo enviado a {transportista.nombre}: La cotización ha sido confirmada con la forma de pago seleccionada.")
