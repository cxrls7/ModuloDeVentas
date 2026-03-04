from src.database.conexion_mysql import obtener_conexion

def guardar_venta_completa(producto, cantidad, precio, total, datos_ia):
    
    
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    sql = """
        INSERT INTO ventas 
        (producto, cantidad, precio_unitario, total, eslogan_ia, categoria, feedback_interno) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    
    
    eslogan, categoria, feedback = datos_ia
    
    valores = (producto, cantidad, precio, total, eslogan, categoria, feedback)
    
    cursor.execute(sql, valores)
    conn.commit()
    conn.close()
    print("✅ Venta e Inteligencia de Negocio guardadas correctamente.")

def obtener_dashboard_trabajador():
 
    conn = obtener_conexion()
    cursor = conn.cursor()
    
   
    sql = """
        SELECT COUNT(*), SUM(total) 
        FROM ventas 
        WHERE DATE(fecha_registro) = CURDATE()
    """
    
    cursor.execute(sql)
    resultado = cursor.fetchone() 
    conn.close()
    
   
    ventas_hoy = resultado[0] if resultado[0] else 0
    ganancia_hoy = resultado[1] if resultado[1] else 0.0
    
    return ventas_hoy, ganancia_hoy