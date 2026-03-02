from src.services.almacenamiento import obtener_ventas

def mostrar_historial():
    ventas = obtener_ventas()

    if not ventas:
        print("\nNo hay ventas registradas en el historial.")
        return
    
    print("\n===== HISTORIAL DE VENTAS =====")

    for i, venta in enumerate(ventas, start=1):
        print(f"\nVenta #{i}")
        print("-----------------")
        for clave, valor in venta.items():
            print(f"{clave}: {valor}")
            