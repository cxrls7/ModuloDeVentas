import mysql.connector

def obtener_conexion():
    try:
        config = {
            'host': 'localhost',
            'user': 'carlos', 
            'password': 'Carlos1050',
            'database': 'modulo_ventas'
        }
        conexion = mysql.connector.connect(**config)
        return conexion
    except mysql.connector.Error as err:
        print(f"❌ Error de conexión: {err}")
        return None