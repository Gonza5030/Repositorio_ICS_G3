# app.py
from views import CotizacionView
from models import Cotizacion, Transportista

def main():
    # Simulación de datos de la cotización
    transportista = Transportista(nombre="Transportista ABC", calificacion=4.8)
    cotizacion = Cotizacion(
        transportista=transportista,
        fecha_retiro="2024-09-10",
        fecha_entrega="2024-09-15",
        importe=2500,
        formas_pago=["Tarjeta", "Contado al retirar", "Contado contra entrega"]
    )

    # Crear vista y ejecutar
    cotizacion_view = CotizacionView(cotizacion)
    cotizacion_view.mostrar_detalles()

if __name__ == "__main__":
    main()
