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

from src.services.ai_service import obtener_analisis_ia
from src.database.queries import obtener_dashboard_trabajador
from src.utils.decorators import manejador_global

@manejador_global # Protege todo el proceso de registro
def registrar_venta():
    print("\n" + "="*20 + " SISTEMA DE VENTAS INTELIGENTE " + "="*20)
    
    while True:
        producto = input("\nIngrese el nombre del producto (o 'salir' para terminar): ").strip()
        
        if producto.lower() == 'salir':
            break

        try:
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio unitario: "))
        except ValueError:
            print("Error‼️ : Debe ingresar valores numéricos válidos.")
            continue 
            
        if cantidad <= 0 or precio <= 0:
            print("Error‼️ : La cantidad y el precio deben ser mayores a 0.")
            continue

        while True:
            vip_input = input("¿El cliente es VIP? (si/no): ").strip().lower()
            if vip_input in ["si", "no"]:
                es_vip = vip_input == "si"
                break
            print("Error‼️ : Por favor ingrese 'si' o 'no'.")

    
        venta = Venta(producto, cantidad, precio, es_vip)
        venta.subtotal = calcular_subtotal(venta.precio_unitario, venta.cantidad)
        venta.descuento = calcular_descuento_vip(venta.subtotal, venta.es_vip)
        venta.total = calcular_total_final(venta.subtotal, venta.descuento)

        
        print("🤖 IA Analizando venta...")
     
        ventas_hoy, _ = obtener_dashboard_trabajador()
        
        datos_ia = obtener_analisis_ia(producto, precio, cantidad, ventas_hoy)
        
        venta.eslogan_ia = datos_ia[0]
        venta.categoria = datos_ia[1]
        venta.feedback_interno = datos_ia[2]

       
        guardar_venta_mysql(venta) 
        
        
        mostrar_resumen_venta(venta)
        
        print(f"\n✅ Venta guardada. Categoría: {venta.categoria}")

def mostrar_resumen_venta(venta):
    print("\n" + "-" * 60)
    print("             RESUMEN DE LA VENTA (IA ENHANCED)")
    print("-" * 60)
    print(f"Producto        : {venta.producto}")
    print(f"Categoría       : {getattr(venta, 'categoria', 'General')}")
    print(f"Cantidad        : {venta.cantidad}")
    print(f"Precio Unitario : {formatear_moneda(venta.precio_unitario)}")
    print("-" * 60)
    print(f"Subtotal        : {formatear_moneda(venta.subtotal)}")
    print(f"Descuento VIP   : {formatear_moneda(venta.descuento)}")
    print("-" * 60)
    print(f"TOTAL A PAGAR   : {formatear_moneda(venta.total)}")