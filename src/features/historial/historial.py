# En src/features/historial/historial.py
from src.utils.formato import formatear_moneda #
from src.services.almacenamiento import obtener_ventas


def mostrar_historial():
   
    ventas = obtener_ventas()

    if not ventas:
        print("\n📭 No hay ventas registradas en la base de datos.")
        return

   
    print("\n" + "=" * 95)
    print(f"{'#':<4} | {'Producto':<20} | {'Cant.':<6} | {'Precio U.':<12} | {'Total':<15} | {'Estado'}")
    print("-" * 95)

    for i, v in enumerate(ventas, 1):
        
        nombre_prod = (v.producto[:17] + '..') if len(v.producto) > 20 else v.producto
        
        print(f"{i:<4} | {nombre_prod:<20} | {v.cantidad:<6} | "
              f"{formatear_moneda(v.precio_unitario):<12} | "
              f"{formatear_moneda(v.total):<15} | "
              f"✅ Guardado")

    print("=" * 95)
    print(f"📊 Resumen: Se encontraron {len(ventas)} transacciones en el sistema.")