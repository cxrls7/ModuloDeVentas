from src.database.conexion_mysql import obtener_conexion


def guardar_venta_mysql(venta):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    cursor.execute("""
        INSERT INTO ventas (producto, cantidad, precio_unitario, es_vip, subtotal, descuento, total)
        VALUES (?, ?, ?, ?, ?, ?, ?) """, (
           venta.producto,
           venta.cantidad,
           venta.precio_unitario,
           venta.es_vip,
           venta.subtotal,
           venta.descuento,
           venta.total
        ))
    conexion.commit()
    conexion.close()

def obtener_ventas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM ventas")
    filas = cursor.fetchall()

    ventas = []

    for fila in filas:
        venta = venta(
            producto=fila[1],
            cantidad=fila[2],
            precio_unitario=fila[3],
            es_vip=bool(fila[4]),
            subtotal=fila[5],
            descuento=fila[6],
            total=fila[7]
        )
        ventas.append(venta)
        
    conexion.close()

    return ventas

