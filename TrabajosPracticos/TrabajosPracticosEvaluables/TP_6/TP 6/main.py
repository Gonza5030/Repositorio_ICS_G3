import os
from flask import Flask, render_template, request
from models.transportista import Transportista
from models.cotizacion import Cotizacion
from utils.pago import validar_tarjeta, procesar_pago
from services.notificaciones import enviar_notificacion_push, enviar_email_confirmacion
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

app = Flask(__name__)

# Obtener el email del transportista desde el .env
transportista_email = os.getenv("EMAIL_USER")

# Datos de prueba (puedes cargarlo de una base de datos en un caso real)
transportista = Transportista("Juan Pérez", 4.7)
cotizacion = Cotizacion(
    transportista,
    "2024-09-10",
    "2024-09-12",
    1500,
    ["tarjeta", "contado al retirar", "contado contra entrega"],
)

@app.route("/")
def index():
    return render_template(
        "cotizacion.html",
        transportista_nombre=cotizacion.transportista.nombre,
        transportista_calificacion=cotizacion.transportista.calificacion,
        fecha_retiro=cotizacion.fecha_retiro,
        fecha_entrega=cotizacion.fecha_entrega,
        importe=cotizacion.importe,
    )

@app.route("/procesar_pago", methods=["POST"])
def procesar_pago_view():
    forma_pago = request.form.get("forma_pago")

    if forma_pago == "tarjeta":
        numero_tarjeta = request.form.get("numero_tarjeta")
        pin = request.form.get("pin")
        nombre_completo = request.form.get("nombre_completo")
        tipo_documento = request.form.get("tipo_documento")
        numero_documento = request.form.get("numero_documento")
        fecha_vto = request.form.get("fecha_vencimiento")

        es_valido, mensaje = validar_tarjeta(
            numero_tarjeta,
            pin,
            nombre_completo,
            tipo_documento,
            numero_documento,
            fecha_vto,
        )
        if not es_valido:
            return mensaje  # Devuelve el mensaje de error de validación

        pago_exitoso, mensaje = procesar_pago("tarjeta", cotizacion.importe)
        if pago_exitoso:
            cotizacion.estado = "Confirmado"
            notificacion_push = enviar_notificacion_push(
                cotizacion.transportista.nombre, forma_pago
            )
            mail = enviar_email_confirmacion(
                cotizacion.transportista.nombre, 
                transportista_email,  
                forma_pago
            )
            return f"Pago procesado correctamente. Número de pago {mensaje}.\n\n{notificacion_push}\n\n{mail}"
        else:
            return f"Pago rechazado: {mensaje}."  # Devuelve el mensaje de saldo insuficiente
    else:
        cotizacion.estado = "Confirmado"

        # Enviar notificación push
        notificacion_push = enviar_notificacion_push(
            cotizacion.transportista.nombre, forma_pago
        )

        # Enviar email al transportista
        mail = enviar_email_confirmacion(
            cotizacion.transportista.nombre,
            transportista_email,  
            forma_pago
        )
        return f"{notificacion_push}\n\n{mail}"

if __name__ == "__main__":
    app.run(debug=True)
