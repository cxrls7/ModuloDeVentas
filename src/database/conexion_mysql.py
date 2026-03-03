import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="ventas_user",
        password="Carlos1050*",
        database="modulo_ventas"
    )