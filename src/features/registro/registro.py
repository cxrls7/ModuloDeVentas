#Este módulo se encarga de registrar las ventas, calcular el subtotal, descuento y total final, y mostrar un resumen de la venta
#Importe las funciones necesarias para el registro de ventas y los cálculos relacionados
#Importe tambien la clase venta para crear objetos de venta y almacenar los detalles de cada transacción

from src.utils.formato import formatear_moneda
from src.models.ventas import Venta
from src.features.validacion.validacion import (
    calcular_subtotal, 
    calcular_descuento_vip, 
    calcular_total_final
)
from src.services.almacenamiento import guardar_venta_mysql

def registrar_venta():
    """Bucle profesional para registrar varias ventas en una sesión."""
    print("\n" + "="*20 + " SISTEMA DE VENTAS " + "="*20)
    
    while True:
        producto = input("\nIngrese el nombre del producto (o 'salir' para terminar): ").strip()
        
        if producto.lower() == 'salir':
            print("\nFinalizando sesión de registro. ¡Hasta pronto!")
            break

        try:
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio unitario: "))
        except ValueError:
            print("Error‼️ : Debe ingresar valores numéricos válidos.")
            continue # Reintenta el registro actual
            
        if cantidad <= 0 or precio <= 0:
            print("Error‼️ : La cantidad y el precio deben ser mayores a 0.")
            continue

        # Validación VIP
        while True:
            vip_input = input("¿El cliente es VIP? (si/no): ").strip().lower()
            if vip_input in ["si", "no"]:
                es_vip = vip_input == "si"
                break
            print("Error‼️ : Por favor ingrese 'si' o 'no'.")

        # 1. Crear el objeto Venta
        venta = Venta(producto, cantidad, precio, es_vip)

        # 2. Realizar cálculos ANTES de guardar (Para que MySQL tenga los totales)
        venta.subtotal = calcular_subtotal(venta.precio_unitario, venta.cantidad)
        venta.descuento = calcular_descuento_vip(venta.subtotal, venta.es_vip)
        venta.total = calcular_total_final(venta.subtotal, venta.descuento)

        # 3. Guardar en MySQL
        guardar_venta_mysql(venta) 
        
        # 4. Mostrar el resumen individual
        mostrar_resumen_venta(venta)
        
        print("\n✅ Venta guardada en la base de datos.")

def mostrar_resumen_venta(venta):
    print("\n" + "-" * 60)
    print("             RESUMEN DE LA VENTA")
    print("-" * 60)
    print(f"Producto        : {venta.producto}")
    print(f"Cantidad        : {venta.cantidad}")
    print(f"Precio Unitario : {formatear_moneda(venta.precio_unitario)}")
    print("-" * 60)
    print(f"Subtotal        : {formatear_moneda(venta.subtotal)}")
    print(f"Descuento VIP   : {formatear_moneda(venta.descuento)}")
    print("-" * 60)
    print(f"TOTAL A PAGAR   : {formatear_moneda(venta.total)}")
    print("-" * 60)