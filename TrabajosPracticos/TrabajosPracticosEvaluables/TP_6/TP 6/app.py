# app.py
from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure
from views import CotizacionView
from models import Cotizacion, Transportista
from notifications import enviar_correo, enviar_notificacion_push

# Crear una instancia de FastAPI
app = FastAPI()

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

# Configurar ReactPy con FastAPI y el componente
configure(app, component=App)

# Ruta principal para la aplicación ReactPy
@app.get("/")
async def get_app():
    return html.div(App())

# Ejecutar el servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)