from src.database.conexion_mysql import obtener_conexion
from src.models.ventas import Venta

def guardar_venta_mysql(venta):
    conexion = obtener_conexion()
    if conexion is None:
        return
        
    try:
        cursor = conexion.cursor()
       
        query = """
            INSERT INTO ventas (producto, cantidad, precio_unitario, es_vip, subtotal, descuento, total)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        valores = (
           venta.producto,
           venta.cantidad,
           venta.precio_unitario,
           venta.es_vip,
           venta.subtotal,
           venta.descuento,
           venta.total
        )
        
        cursor.execute(query, valores)
        conexion.commit()
    except Exception as e:
        print(f"❌ Error al guardar en MySQL: {e}")
    finally:
        cursor.close()
        conexion.close()

def obtener_ventas():
    conexion = obtener_conexion()
    if conexion is None:
        return []

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM ventas")
        filas = cursor.fetchall()

        ventas = []
        for fila in filas:
           
            v = Venta(
                producto=fila[1],
                cantidad=fila[2],
                precio_unitario=fila[3],
                es_vip=bool(fila[4])
            )
          
            v.subtotal = fila[5]
            v.descuento = fila[6]
            v.total = fila[7]
            ventas.append(v)
        
        return ventas
    except Exception as e:
        print(f"❌ Error al obtener ventas: {e}")
        return []
    finally:
        cursor.close()
        conexion.close()

