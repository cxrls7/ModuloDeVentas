from src.database.conexion_mysql import obtener_conexion
from src.models.ventas import Venta
from src.utils.decorators import manejador_global

@manejador_global
def guardar_venta_mysql(venta):
    conexion = None
    cursor = None
    try:
        conexion = obtener_conexion()
        if conexion is None: return
        
        cursor = conexion.cursor()
        
        # Query con las 10 columnas que definimos para la IA
        query = """
            INSERT INTO ventas 
            (producto, cantidad, precio_unitario, es_vip, subtotal, descuento, total, categoria, eslogan_ia, feedback_interno)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        valores = (
            venta.producto,
            venta.cantidad,
            venta.precio_unitario,
            venta.es_vip,
            venta.subtotal,
            venta.descuento,
            venta.total,
            venta.categoria,
            venta.eslogan_ia,
            venta.feedback_interno
        )
        
        cursor.execute(query, valores)
        conexion.commit()
        print(f"✅ Venta guardada en MySQL (ID: {cursor.lastrowid})")
        
    except Exception as e:
        print(f"❌ Error al guardar en DB: {e}")
    finally:
        if cursor: cursor.close()
        if conexion: conexion.close()

@manejador_global
def obtener_ventas():
    conexion = None
    cursor = None
    try:
        conexion = obtener_conexion()
        if conexion is None: return []

        cursor = conexion.cursor()
        # Ordenamos por la fecha que corregimos en MySQL
        cursor.execute("SELECT * FROM ventas ORDER BY fecha_registro DESC")
        filas = cursor.fetchall()

        ventas_cargadas = []
        for fila in filas:
            v = Venta(
                producto=fila[1],
                cantidad=fila[2],
                precio_unitario=fila[3],
                es_vip=bool(fila[4]),
                subtotal=fila[5],   
                descuento=fila[6],  
                total=fila[7],
                categoria=fila[8],        
                eslogan_ia=fila[9],       
                feedback_interno=fila[10] 
            )
            ventas_cargadas.append(v)
        
        return ventas_cargadas
    except Exception as e:
        print(f"❌ Error al leer historial: {e}")
        return []
    finally:
        if cursor: cursor.close()
        if conexion: conexion.close()