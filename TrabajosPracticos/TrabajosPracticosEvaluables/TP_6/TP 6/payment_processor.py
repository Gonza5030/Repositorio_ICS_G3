# payment_processor.py
import random

def procesar_pago(tarjeta, pin, nombre_completo, tipo_documento, numero_documento, tipo_tarjeta):
    # Validaciones básicas
    if len(tarjeta) != 16 or not tarjeta.isdigit():
        print("Número de tarjeta no válido.")
        return False, None

    if len(pin) != 4 or not pin.isdigit():
        print("PIN no válido.")
        return False, None

    # Simulación de saldo suficiente/insuficiente ACORDARME QUE ES TRUE FALSE !!!!!!!!
    tiene_saldo = random.choice([True, False])
    if not tiene_saldo:
        print(f"La tarjeta de {tipo_tarjeta} no tiene saldo suficiente.")
        return False, None

    # Simulación de pago exitoso
    nro_pago = random.randint(1000, 9999)
    return True, nro_pago
