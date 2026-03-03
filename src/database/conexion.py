import sqlite3
import os

RUTA_DB = os.path.join("src", "data", "ventas.db")

def obtener_conexion():
    return sqlite3.connect(RUTA_DB)

def crear_tabla():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio_unitario REAL NOT NULL,
            es_vip BOOLEAN NOT NULL,
            subtotal REAL NOT NULL,
            descuento REAL NOT NULL,
            total REAL NOT NULL) """)
    
    conexion.commit()
    conexion.close()
    