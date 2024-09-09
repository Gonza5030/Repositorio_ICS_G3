# views.py
from reactpy import component, html, use_state
from payment_processor import procesar_pago
from notifications import enviar_correo, enviar_notificacion_push


@component
def CotizacionView(cotizacion):
    forma_pago, set_forma_pago = use_state("")
    estado_cotizacion, set_estado_cotizacion = use_state(cotizacion.estado)
    pago_exitoso, set_pago_exitoso = use_state(None)

    def aceptar_cotizacion(event):
        if estado_cotizacion == "Confirmado":
            print("La cotización ya ha sido confirmada.")
            return
        if forma_pago == "":
            set_pago_exitoso(False)
            print("Debe elegir una forma de pago.")
        elif forma_pago == "Tarjeta":
            procesar_pago_tarjeta()
        else:
            confirmar_cotizacion(forma_pago)

    def procesar_pago_tarjeta():
        # Aquí se simula la entrada de los datos de la tarjeta
        print("Procesando pago con tarjeta...")
        tarjeta_valida, nro_pago = procesar_pago("1234567890123456", "1234", "Juan Perez", "DNI", "12345678", "credito")
        if tarjeta_valida:
            confirmar_cotizacion("Tarjeta")
            set_pago_exitoso(True)
            print(f"Pago exitoso, número de pago: {nro_pago}")
        else:
            set_pago_exitoso(False)
            print("El pago fue rechazado.")

    def confirmar_cotizacion(forma_pago):
        set_estado_cotizacion("Confirmado")
        enviar_notificacion_push(cotizacion.transportista)
        enviar_correo(cotizacion.transportista)
        print(f"¡Cotización confirmada con forma de pago: {forma_pago}!")

    return html.div(
        {"class": "cotizacion-container"},
        html.h2(f"Transportista: {cotizacion.transportista.nombre}"),
        html.p(f"Calificación: {cotizacion.transportista.calificacion}"),
        html.p(f"Fecha de retiro: {cotizacion.fecha_retiro}"),
        html.p(f"Fecha de entrega: {cotizacion.fecha_entrega}"),
        html.p(f"Importe del viaje: {cotizacion.importe}"),
        html.p(f"Formas de pago: {', '.join(cotizacion.formas_pago)}"),

        # Input para seleccionar forma de pago
        html.select(
            {"on_change": lambda event: set_forma_pago(event["target"]["value"])},
            html.option({"value": ""}, "Seleccione una forma de pago"),
            *[html.option({"value": forma}, forma) for forma in cotizacion.formas_pago]
        ),

        html.button({"on_click": aceptar_cotizacion}, "Aceptar cotización"),

        html.p("Estado: " + estado_cotizacion),
        html.p("Pago exitoso" if pago_exitoso else "Pago rechazado")
    )
    