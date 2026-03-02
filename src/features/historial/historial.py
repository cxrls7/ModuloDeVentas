from src.services.almacenamiento import obtener_ventas


def mostrar_historial():
    ventas = obtener_ventas()

    if not ventas:
        print("\nNo hay ventas registradas.")
        return

    print("\n===== HISTORIAL DE VENTAS =====")

    total_general = 0
    total_productos = 0

    for i, venta in enumerate(ventas, start=1):
        print(f"\nVenta #{i}")
        print("----------------------")

        for clave, valor in venta.items():
            print(f"{clave}: {valor}")

        # Suponiendo que tienes cantidad y precio
        subtotal = venta["cantidad"] * venta["precio"]
        total_general += subtotal
        total_productos += venta["cantidad"]

    print("\n===== RESUMEN GENERAL =====")
    print(f"Total productos vendidos: {total_productos}")
    print(f"Total dinero generado: {round(total_general)}")