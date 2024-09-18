import re
from datetime import datetime
import random


def validar_tarjeta(numero_tarjeta, pin, nombre_completo, tipo_documento, numero_documento, fecha_vencimiento):
    # Validar cada campo
    pin_valid = re.match(r'^\d{4}$', pin)
    tarjeta_valid = re.match(r'^\d{16}$', numero_tarjeta)
    nombre_valid = re.match(r'^[A-Za-z\s]+$', nombre_completo)
    documento_valid = re.match(r'^\d+$', numero_documento)
    vencimiento_valid = re.match(r'^\d{2}/\d{2}$', fecha_vencimiento)

    if not all([pin_valid, tarjeta_valid, nombre_valid, documento_valid, vencimiento_valid]):
        return False, "Error en datos de la tarjeta."
    
    # Validar que la fecha de vencimiento es futura
    try:
        mes, anio = map(int, fecha_vencimiento.split('/'))
        if 0 > mes or mes > 13:
            return False, "Mes inválido"
        fecha_vto = datetime(year=anio + 2000, month=mes, day=1)
        if fecha_vto < datetime.now():
            return False, "Tarjeta vencida."
    except ValueError:
        return False, "Tarjeta vencida."
    return True, "Datos correctos de la tarjeta."


def procesar_pago(metodo_pago, importe):
    # Simular una verificación de saldo
    saldo_disponible = 2000  # Ejemplo: el saldo de la tarjeta es $2000, hardcodeado
    
    if metodo_pago == "tarjeta" and importe > saldo_disponible:
        return False, "Saldo insuficiente"  # Pago rechazado por saldo insuficiente
    
    # Si el pago es exitoso, generamos un número de transacción aleatorio
    numero_transaccion = str(random.randint(100000000, 999999999))  # Número aleatorio de 9 dígitos

    # Si el pago es exitoso, devolvemos el número de transacción
    return True, numero_transaccion  
