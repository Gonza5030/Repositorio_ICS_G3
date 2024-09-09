class Cotizacion:
    def __init__(self, transportista, fecha_retiro, fecha_entrega, importe, formas_pago):
        self.transportista = transportista
        self.fecha_retiro = fecha_retiro
        self.fecha_entrega = fecha_entrega
        self.importe = importe
        self.formas_pago = formas_pago
        self.estado = 'Pendiente'