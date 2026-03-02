from src.services.almacenamiento import obtener_ventas


def formatear_moneda(valor):
    return f"{valor:,.0f}".replace(",", ".")


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

        es_vip_texto = "Sí" if venta["es_vip"] else "No"

        print(f"Producto: {venta['producto']}")
        print(f"Cantidad: {venta['cantidad']}")
        print(f"Precio unitario: $ {formatear_moneda(venta['precio_unitario'])}")
        print(f"Es VIP: {es_vip_texto}")
        print(f"Subtotal: $ {formatear_moneda(venta['subtotal'])}")
        print(f"Descuento: $ {formatear_moneda(venta['descuento'])}")
        print(f"Total: $ {formatear_moneda(venta['total'])}")

        total_general += venta["total"]
        total_productos += venta["cantidad"]

    print("\n===== RESUMEN GENERAL =====")
    print(f"Total productos vendidos: {total_productos}")
    print(f"Total dinero generado: $ {formatear_moneda(total_general)}")