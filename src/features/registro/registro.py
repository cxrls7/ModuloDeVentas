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

def registrar_venta():
    print("\n" + "═"*20 + " REGISTRO DE VENTA " + "═"*20)
    
   
    producto = input("📦 Nombre del producto: ").strip()
    if not producto:
        print("❌ El nombre no puede estar vacío.")
        return

    try:
        cantidad = int(input("🔢 Cantidad: "))
        precio = float(input("💰 Precio Unitario: "))
        if cantidad <= 0 or precio <= 0:
            print("❌ Los valores deben ser mayores a cero.")
            return
    except ValueError:
        print("❌ Error: Ingrese solo números para cantidad y precio.")
        return

    es_vip = input("🌟 ¿Es cliente VIP? (si/no): ").strip().lower() == "si"

    
    sub_calc = calcular_subtotal(precio, cantidad)
    desc_calc = calcular_descuento_vip(sub_calc, es_vip)
    total_calc = calcular_total_final(sub_calc, desc_calc)

   
    print("🧠 Consultando cerebro de IA...") 
    res_ia = obtener_analisis_ia(producto, precio, cantidad, 0)

    
    nueva_venta = Venta(
        producto=producto,
        cantidad=cantidad,
        precio_unitario=precio,
        es_vip=es_vip,
        subtotal=sub_calc,      
        descuento=desc_calc,   
        total=total_calc,       
        eslogan_ia=res_ia[0],
        feedback_interno=res_ia[2]
    )

   
    guardar_venta_mysql(nueva_venta)

  
    mostrar_ticket(nueva_venta)

def mostrar_ticket(venta):
    print("\n" + "─"*40)
    print(f"       RESUMEN DE OPERACIÓN")
    print("─"*40)
    print(f" ARTÍCULO : {venta.producto.upper()}")
    print(f" CATEGORÍA: {venta.categoria}")
    print(f" CANTIDAD : {venta.cantidad}")
    print(f" SUBTOTAL : {formatear_moneda(venta.subtotal)}")
    print(f" DESC. VIP: -{formatear_moneda(venta.descuento)}")
    print(f" TOTAL    : {formatear_moneda(venta.total)}")
    print("─"*40)
    print(f" 📣 IA: \"{venta.eslogan_ia}\"")
    print("─"*40 + "\n")