# utils/pago.py
def validar_tarjeta(numero_tarjeta, pin, nombre_completo, tipo_documento, numero_documento):
    # Aquí agregamos la validación básica de los datos de la tarjeta
    if len(numero_tarjeta) == 16 and len(pin) == 4 and nombre_completo and tipo_documento and numero_documento:
        return True
    return False

def procesar_pago(metodo_pago, importe):
    # Simular una verificación de saldo
    saldo_disponible = 2000  # Ejemplo: el saldo de la tarjeta es $1000
    
    if metodo_pago == "tarjeta" and importe > saldo_disponible:
        return False, "Saldo insuficiente"  # Pago rechazado por saldo insuficiente
    
    # Si el pago es exitoso, devolvemos el número de transacción
    return True, "123456789"  # Ejemplo: número de transacción exitosa
