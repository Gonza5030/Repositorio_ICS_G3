# app.py
from reactpy import component, html, run
from views import CotizacionView
from models import Cotizacion, Transportista
from notifications import enviar_correo, enviar_notificacion_push

# Componente principal de la aplicación ReactPy
@component
def App():
    # Crear un objeto de transportista
    transportista = Transportista(nombre="Transportista ABC", calificacion=4.8)

    # Datos de ejemplo de la cotización
    cotizacion = Cotizacion(
        transportista=transportista,
        fecha_retiro="2024-09-10",
        fecha_entrega="2024-09-12",
        importe=100.0,
        formas_pago=['Tarjeta', 'Contado al retirar', 'Contado contra entrega'],
        estado='Pendiente'
    )

    # Crear la vista de cotización
    return CotizacionView(cotizacion)

# Ejecutar el servidor de ReactPy
if __name__ == "__main__":
    run(App,  "static")
