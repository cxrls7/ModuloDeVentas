from src.database.conexion_mysql import obtener_conexion
from src.models.ventas import Venta
from src.utils.decorators import manejador_global

@manejador_global
def guardar_venta_mysql(venta):
    conexion = obtener_conexion()
    if conexion is None: return
        
    cursor = conexion.cursor()
    
   
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
        getattr(venta, 'categoria', 'General'),
        getattr(venta, 'eslogan_ia', ''),
        getattr(venta, 'feedback_interno', '')
    )
    
    cursor.execute(query, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

@manejador_global
def obtener_ventas():
    conexion = obtener_conexion()
    if conexion is None: return []

    cursor = conexion.cursor()
   
    cursor.execute("SELECT * FROM ventas ORDER BY fecha_registro DESC")
    filas = cursor.fetchall()

    ventas = []
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
        )