# views.py
from payment_processor import procesar_pago
from notifications import enviar_notificacion_push, enviar_correo


class CotizacionView:
    def __init__(self, cotizacion):
        self.cotizacion = cotizacion
        self.forma_pago_seleccionada = None

    def mostrar_detalles(self):
        if self.cotizacion.estado == "Confirmado":
            print("Esta cotización ya ha sido confirmada. No se puede modificar.")
            return

        print(f"Transportista: {self.cotizacion.transportista.nombre}")
        print(f"Calificación: {self.cotizacion.transportista.calificacion}")
        print(f"Fecha de retiro: {self.cotizacion.fecha_retiro}")
        print(f"Fecha de entrega: {self.cotizacion.fecha_entrega}")
        print(f"Importe del viaje: {self.cotizacion.importe}")
        print(f"Formas de pago disponibles: {', '.join(self.cotizacion.formas_pago)}")

        self.elegir_forma_pago()

    def elegir_forma_pago(self):
        forma_pago = input("Elija una forma de pago: ").strip()

        if not forma_pago:
            print("Debe elegir una forma de pago. Intente de nuevo.")
            return self.elegir_forma_pago()

        if forma_pago not in self.cotizacion.formas_pago:
            print("Forma de pago no válida. Intente de nuevo.")
            return self.elegir_forma_pago()

        self.forma_pago_seleccionada = forma_pago

        if forma_pago == "Tarjeta":
            self.procesar_pago_tarjeta()
        else:
            self.confirmar_cotizacion(forma_pago)

    def procesar_pago_tarjeta(self):
        tarjeta = input("Ingrese el número de la tarjeta: ").strip()
        if not tarjeta:
            print("Número de tarjeta no válido.")
            return self.elegir_forma_pago()

        pin = input("Ingrese el PIN de la tarjeta: ").strip()
        if not pin:
            print("PIN no válido.")
            return self.elegir_forma_pago()

        nombre_completo = input("Ingrese el nombre completo: ").strip()
        if not nombre_completo:
            print("Nombre no válido.")
            return self.elegir_forma_pago()

        tipo_documento = input("Ingrese el tipo de documento: ").strip()
        if not tipo_documento:
            print("Tipo de documento no válido.")
            return self.elegir_forma_pago()

        numero_documento = input("Ingrese el número de documento: ").strip()
        if not numero_documento:
            print("Número de documento no válido.")
            return self.elegir_forma_pago()

        tipo_tarjeta = input("¿Es una tarjeta de crédito o débito? ").strip().lower()
        exito, nro_pago = procesar_pago(
            tarjeta, pin, nombre_completo, tipo_documento, numero_documento, tipo_tarjeta
        )

        if exito:
            print(f"Pago procesado correctamente. Número de pago: {nro_pago}")
            self.confirmar_cotizacion("Tarjeta")
        else:
            print("El pago fue rechazado. Intente con otra tarjeta o elija otro método de pago.")
            self.elegir_forma_pago()

    def confirmar_cotizacion(self, forma_pago):
        if self.cotizacion.estado == "Confirmado":
            print("Esta cotización ya ha sido confirmada. No se puede modificar.")
            return

        self.cotizacion.estado = "Confirmado"
        print(f"¡Cotización confirmada! Forma de pago: {forma_pago}")

        # Enviar notificaciones
        enviar_notificacion_push(self.cotizacion.transportista)
        enviar_correo(self.cotizacion.transportista)
